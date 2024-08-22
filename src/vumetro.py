"""Este módulo define un widget de un vúmetro de audio para PySide6

El widget sirve para representar de manera gráfica los niveles de audio 
captado a través de un micrófono en tiempo real

Este widget puede ser promocionado y usado en QtDesigner para PySide6

El widget tiene numerosos parámetros de configuración entre los que se 
encuentran los que modifican la apariencia física y los que modifican la
manera de recibir la señal de audio
"""
import math
import struct
import threading
import pyaudio
import re
from enum import Enum

from PySide6.QtCore import QRect, Qt, QSize, QPoint, QRectF
from PySide6.QtGui import QBrush, QPen, QColor, QFont, QPainter, QPainterPath, QLinearGradient
from PySide6.QtWidgets import QLCDNumber, QWidget


class PowerBar(QWidget):
    ''' Clase que representa al módulo entero

    En esta clase se encuentra todos los atributos y funciones usadas
    para el funcionamiento del widget y que permiten cambiar su comportamiento

    Args:
        QWidget (QWidget): Clase de la que hereda y que permite usarla como un widget

    Attributes:
        RATE (int): Frecuencia de muestreo del audio
        INPUT_BLOCK_TIME (float): Tiempo que se tarda en captar el audio
        INPUT_FRAMES_PER_BLOCK (int): Numero de frames que se captan en el tiempo INPUT_BLOCK_TIME
        encendido (bool): Indica si el vúmetro está activo
        estiloVumetro (int): Indica el estilo de vúmetro que se quiere
        directionVumetroBarras (int): Indica la dirección de las barras del vúmetro
        number_bars (int): Numero de barras que se quieren mostrar
        calibracion_db (int): Factor de escala que se le quiere aplicar al audio captado por el micrófono
        range_detection (int): Rango máximo de volumen que se quiere representar gráficamente en el vúmetro
        minimal_detection (int): Valor mínimo de detección del vúmetro
        volumen (int): Volumen normalizado actual del vúmetro
        espectroVolumen (list of int): Lista que guarda el espectro de volumen
        padding_barras (int): Espacio entre la representación gráfica del audio y el borde del lienzo
        solid_percent (float): Porcentaje de espacio entre barras
        background_color (str): Color de fondo del vúmetro
        bar_color (str): Color de la representación grafica del audio
        actulizacionConfiguracion (bool): Controla que el estilo ESPECTRO se actualice correctamente al realizar cambios en la configuración
    '''
    RATE = 44000
    INPUT_BLOCK_TIME = 0.1  
    INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
    encendido = False
    estiloVumetro = 0
    directionVumetroBarras = 0
    number_bars = 18
    calibracion_db = 50
    range_detection = 45
    minimal_detection = 0
    volumen = 0
    espectroVolumen = [0] * number_bars
    padding_barras = 5
    solid_percent = 0.7
    background_color = '#000000'
    bar_color = ['#00BFFF']
    actulizacionConfiguracion = False

    class EstiloVumetro(Enum):
        '''Clase de Enum para elegir el tipo de vúmetro

            Args:
                Enum (Enum): Clase de la que hereda para hacer una clase enum con constantes

            Attributes:
                BARRAS (int): Indica que el estilo de vúmetro es el de barras
                CIRCULOS (int): Indica que el estilo de vúmetro es el de círculos
                ESPECTRO (int): Indica que el estilo de vúmetro es el de un espectrograma de audio
                ANGULO (int): Indica que el estilo de vúmetro es el de ángulo
        '''
        BARRAS = 0
        CIRCULOS = 1
        ESPECTRO = 2
        ANGULO = 3

    class DirectionVumetroBarras(Enum):
        '''Clase de Enum para elegir la dirección del vúmetro
            Args:
                Enum (Enum): Clase de la que hereda para hacer una clase enum con constantes

            Attributes:
                ARRIBA (int): Indica que la dirección del vúmetro es hacia arriba
                DERECHA (int): Indica que la dirección del vúmetro es hacia la derecha
                ABAJO (int): Indica que la dirección del vúmetro es hacia abajo
                IZQUIERDA (int): Indica que la dirección del vúmetro es hacia la izquierda
        '''
        ARRIBA = 0
        DERECHA = 1
        ABAJO = 2
        IZQUIERDA = 3

    def __init__(self, *args, **kwargs):
        '''Llama a dos funciones para crear un objeto QLCDNumber e inicializa el vúmetro'''
        super().__init__(*args, **kwargs)
        self.__init__lcd()
        self.activar_vumetro()

    def __init__lcd(self):
        self.lcd_volumen = QLCDNumber()
        self.lcd_volumen.setObjectName(u"lcd_volumen")
        self.lcd_volumen.setMinimumSize(QSize(0, 23))
        font = QFont()
        font.setBold(False)
        self.lcd_volumen.setFont(font)
        self.lcd_volumen.setStyleSheet(u"")
        self.lcd_volumen.setDigitCount(3)
        self.lcd_volumen.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_volumen.setProperty("intValue", 0)

    def activar_vumetro(self):
        '''Activa el vúmetro.

        Si el vúmetro no está ya activo, inicia un nuevo hilo que ejecuta el método start_audio_capture del vúmetro
        '''
        if not self.encendido:
            hilo_vumetro = threading.Thread(target=self.start_audio_capture)
            hilo_vumetro.start()
            self.encendido = True

    def desactivar_vumetro(self):
        '''Detiene el vúmetro

        Establece la variable encendido a False para que el hilo que ejecuta el método start_audio_capture del vúmetro termine
        '''
        self.encendido = False

    def get_volumen(self) -> int:
        """Obtiene el volumen normalizado actual del vúmetro

        Returns:
            int: El volumen actual del vúmetro
        """
        return self.volumen

    def set_lcd_calibrarDB(self, db: int):
        """Cambia el factor de escala que se usa para normalizar el volumen

        Esto sirve para calibrar el micrófono y que el valor calculado se aproxime lo máximo posible al real

        Args:
            db (int): Factor de escala que se le quiere aplicar al audio captado por el micrófono
        """
        if db < 1:
            db = 1
        self.calibracion_db = db

    def set_lcd_calibrarRango(self, rango: int):
        """Cambia rango máximo de volumen que se quiere representar gráficamente en el vúmetro

        Esto sirve para calibrar el vúmetro y que muestre el rango de volumen que se desee, apreciando más o menos detalle en la variación de volumen en la representación grafica.

        Args:
            rango (int): Range máximo de volumen que se quiere representar gráficamente en el vúmetro
        """
        if rango < 1:
            rango = 1
        self.range_detection = rango

    def setBackgroundColor(self, color: str):
        """Cambia el color de fondo del vúmetro

        El método recibe un String con el color en formato hexadecimal y lo establece como el color de fondo del vúmetro

        En caso de que el String no sea un color valido, no se hace ningún cambio

        Args:
            color (str): Color en formato hexadecimal
        """
        if not re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            return
        self.background_color = color
        self.actulizacionConfiguracion = True
        self.update()

    def setBarColor(self, color: str):
        """Cambia el color del vúmetro

        Cambia el color de la representación gráfica del audio captado por el micrófono

        El método recibe un String con uno o varios colores en formato hexadecimal separados por comas y lo establece como el/los colores usados para representar el audio

        En caso de que el String no contenga un color valido, no se hace ningún cambio

        El color/colores se guardan como un array de Strings con los colores en formato hexadecimal

        Args:
            color (str): Color en formato hexadecimal
        """
        array_color = color.split(',')
        for i in range(len(array_color)):
            array_color[i] = array_color[i].strip()
            if not re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', array_color[i]):
                return
        self.bar_color = array_color
        self.actulizacionConfiguracion = True
        self.update()

    def setStep(self, step: int):
        """Recibe el número de máximo elementos que se quieren mostrar en el vúmetro

        En el caso del estilo vúmetro barras, este número indica el número máximo de barras que se quieren mostrar

        Args:
            step (int): número de elementos que representan el volumen
        """
        if step < 1:
            step = 1
        self.number_bars = step
        self.espectroVolumen = [0] * step
        self.actulizacionConfiguracion = True
        self.update()

    def setSolidPercent(self, percent: float):
        '''Cambia el porcentaje de espacio entre barras

        Este método recibe un numero entre 0 y 1 que indica el porcentaje de espacio que se quiere entre las barras del vúmetro

        Args:
            percent (float): Porcentaje de espacio entre barras
        '''
        if percent < 0.1:
            percent = 0.1
        elif percent > 0.9:
            percent = 0.9
        self.solid_percent = percent
        self.actulizacionConfiguracion = True
        self.update()

    def changeStyleVumetro(self, estilo: EstiloVumetro):
        '''Cambia el estilo del vúmetro

        Este método recibe un objeto de la clase EstiloVumetro que indica el estilo que se quiere para el vúmetro

        Args:
            estilo (EstiloVumetro): Estilo que se quiere para el vúmetro
        '''
        self.estiloVumetro = estilo.value
        self.update()

    def setDirectionVumetroBarras(self, direction: DirectionVumetroBarras):
        '''Cambia la dirección del vúmetro en los estilos que permiten esta configuración

        Este método recibe un objeto de la clase DirectionVumetroBarras que indica la dirección que desde donde parte la representación grafica del audio

        Args:
            direction (DirectionVumetroBarras): Dirección del vúmetro
        '''
        self.directionVumetroBarras = direction.value
        self.actulizacionConfiguracion = True
        self.update()

    def setMinDetection(self, minimal: int):
        '''Cambia el valor mínimo de detección del vúmetro

        Cambia el valor mínimo de detección del vúmetro, es decir, el valor mínimo que se quiere que se represente gráficamente

        Args:
            minimal (int): Valor mínimo de detección del vúmetro
        '''
        if minimal < 0:
            minimal = 0

        self.minimal_detection = minimal
        self.actulizacionConfiguracion = True
        self.update()

    def set_vumeter_speed(self, speed: int):
        '''Cambia la velocidad de detección del vúmetro

        Cambia la velocidad de detección del vúmetro, es decir, el tiempo que se tarda en actualizar la representación grafica del audio

        Args:
            speed (int): Velocidad de detección del vúmetro
        '''
        if speed < 1:
            speed = 1
        elif speed > 25:
            speed = 25

        self.INPUT_BLOCK_TIME = float(speed) / 100
        self.INPUT_FRAMES_PER_BLOCK = int(self.RATE * self.INPUT_BLOCK_TIME)

    def calculate_volume(self, audio_data):
        '''Método que calcula el volumen del audio captado por el micrófono

        Args:
            audio_data (bytes): Datos de audio captados por el micrófono
        '''
        NORMALIZE_FACTOR = 1.0 / 32768.0
        num_samples = len(audio_data) / 2
        audio_samples = struct.unpack("%dh" %num_samples, audio_data)
        sum_of_squares = sum((s * NORMALIZE_FACTOR) ** 2 for s in audio_samples)
        return math.sqrt(sum_of_squares / num_samples)

    def start_audio_capture(self):
        '''Método que se ejecuta en un hilo para captar el audio del micrófono y calcular el volumen

        Este método se ejecuta en un hilo para que no bloquee la interfaz gráfica y pueda seguir funcionando mientras se captura el audio del micrófono y se calcula el volumen

        El método usa la librería PyAudio para captar el audio del micrófono y la clase Amplitude para calcular el volumen del audio captado

        El volumen calculado se asigna al QLCDNumber self.lcd_volumen y se actualiza la representación gráfica del audio en el vúmetro

        El método termina cuando la variable encendido es False

        Llama a la función update para actualizar la representación gráfica del audio en el vúmetro
        '''
        audio = pyaudio.PyAudio()
        try:

            stream = audio.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=self.RATE,
                                input=True,
                                frames_per_buffer=self.INPUT_FRAMES_PER_BLOCK,
                                )

            max_amplitude  = 0
            while True:
                if not self.encendido:
                    return

                try:
                    audio_data = stream.read(self.INPUT_FRAMES_PER_BLOCK)

                    current_amplitude = self.calculate_volume(audio_data)

                    if current_amplitude > max_amplitude :
                        max_amplitude  = current_amplitude

                    self.volumen = int(current_amplitude * self.calibracion_db)
                    print(self.volumen)
                    self.lcd_volumen.display(self.volumen)
                    self.update()

                except IOError as e:
                    print(f"Error al leer el audio: {e}")
                    continue

        except Exception as e:
            print(f"Error al abrir el stream de audio: {e}")

        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()

    def paintEvent(self, e):
        '''Método que se ejecuta cuando se quiere actualizar la representación gráfica del vúmetro

        El método pinta la representación gráfica del audio en el vúmetro según el estilo que se haya elegido

        Usa las variables de configuración del vúmetro para pintar la representación gráfica del audio según el estilo que se haya elegido

        Args:
            e (QPaintEvent): Evento de pintado
        '''
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(self.background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        if self.volumen > self.range_detection:
            volumen_con_tope = self.range_detection
        else:
            volumen_con_tope = self.volumen

        if (self.range_detection <= self.minimal_detection or self.volumen <= self.minimal_detection) and self.estiloVumetro != 2:
            # painter.end()
            return

        if self.range_detection <= self.minimal_detection or self.volumen < self.minimal_detection:
            volumen_con_tope = self.minimal_detection

        volumen_normalizado = (volumen_con_tope - self.minimal_detection) / \
            (self.range_detection - self.minimal_detection)
        n_steps_to_draw = int(volumen_normalizado * self.number_bars)

        # dimensiones del lienzo
        d_height = painter.device().height() - (self.padding_barras * 2)
        d_width = painter.device().width() - (self.padding_barras * 2)

        if self.estiloVumetro == 0:
            self.pintar_barras(painter, d_height, d_width, n_steps_to_draw, brush)
        elif self.estiloVumetro == 1:
            self.pintar_circulos(painter, d_height, d_width, n_steps_to_draw)
        elif self.estiloVumetro == 2:
            self.pintar_espectro(painter, d_height, d_width, brush, volumen_normalizado)
        elif self.estiloVumetro == 3:
            self.pintar_angulo(painter, d_height, d_width, volumen_normalizado)

        painter.end()

    def pintar_barras(self, painter: QPainter, d_height: int, d_width: int, n_steps_to_draw: int, brush: QBrush):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de barras

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de barras y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            n_steps_to_draw (int): Numero de barras que se quieren pintar
            brush (QBrush): Pincel que se usa para pintar la representación gráfica del audio en el vúmetro
        '''
        # divisiones del lienzo
        step_size_vertical = d_height / self.number_bars
        setp_size_horizontal = d_width / self.number_bars
        # alto barras
        bar_height_vertical = step_size_vertical * self.solid_percent
        bar_height_horizontal = setp_size_horizontal * self.solid_percent
        # Espacio entre barras
        bar_spacer_vertical = (step_size_vertical - bar_height_vertical) / 2
        bar_spacer_horizontal = (
            setp_size_horizontal - bar_height_horizontal) / 2

        for n in range(n_steps_to_draw):
            nextColor = (int)(n // (self.number_bars / len(self.bar_color)))
            # Un color por barra
            brush.setColor(QColor(self.bar_color[nextColor]))
            if self.directionVumetroBarras == 0:
                rect = QRect(
                    self.padding_barras,
                    self.padding_barras + d_height -
                    ((n+1) * step_size_vertical) + bar_spacer_vertical,
                    d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 1:
                rect = QRect(
                    self.padding_barras + (n * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    self.padding_barras,
                    bar_height_horizontal,
                    d_height
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 2:
                rect = QRect(
                    self.padding_barras,
                    self.padding_barras + (n * step_size_vertical) +
                    bar_spacer_vertical,
                    d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 3:
                rect = QRect(
                    self.padding_barras + d_width -
                    ((n+1) * setp_size_horizontal) + bar_spacer_horizontal,
                    self.padding_barras,
                    bar_height_horizontal,
                    d_height
                )
                painter.fillRect(rect, brush)

    def pintar_circulos(self, painter: QPainter, d_height: int, d_width: int, n_steps_to_draw: int):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de círculos

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de círculos y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            n_steps_to_draw (int): Numero de círculos que se quieren pintar
        '''
        diametroMax = min(d_height, d_width) - 2 * self.padding_barras
        step_size = (diametroMax/2) / self.number_bars
        width_pen = step_size * self.solid_percent
        width_spacer = step_size - width_pen
        pen = QPen()
        pen.setWidth(width_pen)
        centroX = d_width / 2 + 2 * self.padding_barras
        centroY = d_height / 2 + 2 * self.padding_barras

        for n in range(n_steps_to_draw):
            nextColor = (int)(n // (self.number_bars / len(self.bar_color)))
            pen.setColor(QColor(self.bar_color[nextColor]))
            painter.setPen(pen)
            painter.drawEllipse(
                centroX - (n+1) * width_pen - n * width_spacer,
                centroY - (n+1) * width_pen - n * width_spacer,
                (2*n+1) * width_pen + (2*n) * width_spacer,
                (2*n+1) * width_pen + (2*n) * width_spacer
            )

    def pintar_espectro(self, painter: QPainter, d_height: int, d_width: int, brush: QBrush, volumen_normalizado: float):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de espectro

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de espectro y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            brush (QBrush): Pincel que se usa para pintar la representación gráfica del audio en el vúmetro
            volumen_normalizado (float): Volumen a mostrar escalado entre cero y uno
        '''
        # divisiones del lienzo
        step_size_vertical = d_height / self.number_bars
        setp_size_horizontal = d_width / self.number_bars
        # alto barras
        bar_height_vertical = step_size_vertical * self.solid_percent
        bar_height_horizontal = setp_size_horizontal * self.solid_percent
        # Espacio entre barras
        bar_spacer_vertical = (step_size_vertical - bar_height_vertical) / 2
        bar_spacer_horizontal = (
            setp_size_horizontal - bar_height_horizontal) / 2

        centroX = d_width / 2
        centroY = d_height / 2
        if not self.actulizacionConfiguracion:
            self.espectroVolumen.pop(0)
            self.espectroVolumen.append(volumen_normalizado+0.01)
        self.actulizacionConfiguracion = False

        for n in range(len(self.espectroVolumen)):
            nextColor = (int)(n // (self.number_bars / len(self.bar_color)))
            # Un color por barra
            brush.setColor(QColor(self.bar_color[nextColor]))
            if self.directionVumetroBarras == 0:
                rect = QRect(
                    centroX - (self.espectroVolumen[n] * centroX),
                    self.padding_barras +
                    (n * step_size_vertical) + bar_spacer_vertical,
                    self.espectroVolumen[n] * d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 1:
                rect = QRect(
                    self.padding_barras + d_width - ((n+1) * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    centroY - (self.espectroVolumen[n] * centroY),
                    bar_height_horizontal,
                    self.espectroVolumen[n] * d_height
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 2:
                rect = QRect(
                    centroX - (self.espectroVolumen[n] * centroX),
                    self.padding_barras + d_height -
                    ((n+1) * step_size_vertical) + bar_spacer_vertical,
                    self.espectroVolumen[n] * d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.directionVumetroBarras == 3:
                rect = QRect(
                    self.padding_barras + (n * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    centroY - (self.espectroVolumen[n] * centroY),
                    bar_height_horizontal,
                    self.espectroVolumen[n] * d_height
                )
                painter.fillRect(rect, brush)

    def pintar_angulo(self, painter: QPainter, d_height: int, d_width: int, volumen_normalizado: float):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de ángulo

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de ángulo y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            volumen_normalizado (float): Volumen a mostrar escalado entre cero y uno
            '''
        diametroMax = min(d_height, d_width) - 2 * self.padding_barras
        center = QPoint(d_width / 2 + self.padding_barras,
                        d_height / 2 + self.padding_barras)
        boundingRect = QRectF(d_width / 2 + self.padding_barras - diametroMax / 2, d_height / 2 + self.padding_barras - diametroMax / 2, diametroMax, diametroMax)
        startAngle = 0
        finalAngle = volumen_normalizado * 360
        sweepLength = 360 / self.number_bars
        cantidad_pintado = int(finalAngle / sweepLength)

        for i in range(cantidad_pintado):
            nextColor = (int)(i // (self.number_bars / len(self.bar_color)))
            if nextColor >= len(self.bar_color):
                break
            painter.setPen(QPen(self.bar_color[nextColor]))
            myPath = QPainterPath()
            myPath.moveTo(center)
            myPath.arcTo(boundingRect, startAngle +
                         i * sweepLength, sweepLength)

            myGradient = QLinearGradient(0, 0, self.width(), self.height())
            myGradient.setColorAt(0.0, QColor(self.bar_color[nextColor]))
            myGradient.setColorAt(1.0, QColor(self.bar_color[nextColor]))

            painter.setBrush(myGradient)
            painter.drawPath(myPath)
