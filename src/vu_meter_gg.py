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


class VUMeterGG(QWidget):
    ''' Clase que representa al módulo entero

    En esta clase se encuentra todos los atributos y funciones usadas
    para el funcionamiento del widget y que permiten cambiar su comportamiento

    Args:
        QWidget (QWidget): Clase de la que hereda y que permite usarla como un widget

    Attributes:
        SAMPLE_RATE (int): Frecuencia de muestreo del audio
        INPUT_BLOCK_TIME (float): Tiempo que se tarda en captar el audio
        INPUT_FRAMES_PER_BLOCK (int): Numero de frames que se captan en el tiempo INPUT_BLOCK_TIME
        vu_meter_on (bool): Indica si el vúmetro está activo
        vu_meter_style (int): Indica el estilo de vúmetro que se quiere
        bars_direction (int): Indica la dirección de las barras del vúmetro
        num_bars (int): Numero de barras que se quieren mostrar
        calibration_db (int): Factor de escala que se le quiere aplicar al audio captado por el micrófono
        max_detection_range (int): Rango máximo de volumen que se quiere representar gráficamente en el vúmetro
        min_detection_level (int): Valor mínimo de detección del vúmetro
        volume_level (int): Volumen normalizado actual del vúmetro
        volume_spectrum (list of int): Lista que guarda el espectro de volumen
        bars_padding (int): Espacio entre la representación gráfica del audio y el borde del lienzo
        bars_solid_percentage (float): Porcentaje de espacio entre barras
        background_color (str): Color de fondo del vúmetro
        bars_color (str): Color de la representación grafica del audio
        configuration_update (bool): Controla que el estilo ESPECTRO se actualice correctamente al realizar cambios en la configuración
    '''
    SAMPLE_RATE = 44000
    INPUT_BLOCK_TIME = 0.1  
    INPUT_FRAMES_PER_BLOCK = int(SAMPLE_RATE*INPUT_BLOCK_TIME)
    vu_meter_on = False
    vu_meter_style = 0
    bars_direction = 0
    num_bars = 18
    calibration_db = 50
    max_detection_range = 45
    min_detection_level = 0
    volume_level = 0
    volume_spectrum = [0] * num_bars
    bars_padding = 5
    bars_solid_percentage = 0.7
    background_color = '#000000'
    bars_color = ['#00BFFF']
    configuration_update = False

    class VUMeterStyle(Enum):
        '''Clase de Enum para elegir el tipo de vúmetro

            Args:
                Enum (Enum): Clase de la que hereda para hacer una clase enum con constantes

            Attributes:
                BARS (int): Indica que el estilo de vúmetro es el de barras
                CIRCLES (int): Indica que el estilo de vúmetro es el de círculos
                SPECTRUM (int): Indica que el estilo de vúmetro es el de un espectrograma de audio
                ANGLE (int): Indica que el estilo de vúmetro es el de ángulo
        '''
        BARS = 0
        CIRCLES = 1
        SPECTRUM = 2
        ANGLE = 3

    class VUMeterBarsDirection(Enum):
        '''Clase de Enum para elegir la dirección del vúmetro
            Args:
                Enum (Enum): Clase de la que hereda para hacer una clase enum con constantes

            Attributes:
                UP (int): Indica que la dirección del vúmetro es hacia arriba
                RIGHT (int): Indica que la dirección del vúmetro es hacia la derecha
                DOWN (int): Indica que la dirección del vúmetro es hacia abajo
                LEFT (int): Indica que la dirección del vúmetro es hacia la izquierda
        '''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    def __init__(self, *args, **kwargs):
        '''Llama a dos funciones para crear un objeto QLCDNumber e inicializa el vúmetro'''
        super().__init__(*args, **kwargs)
        self.__init__lcd()
        self.activate_vu_meter()

    def __init__lcd(self):
        self.lcd_volume = QLCDNumber()
        self.lcd_volume.setObjectName(u"lcd_volume")
        self.lcd_volume.setMinimumSize(QSize(0, 23))
        font = QFont()
        font.setBold(False)
        self.lcd_volume.setFont(font)
        self.lcd_volume.setStyleSheet(u"")
        self.lcd_volume.setDigitCount(3)
        self.lcd_volume.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_volume.setProperty("intValue", 0)

    def get_volume_level(self) -> int:
        """Obtiene el volumen normalizado actual del vúmetro

        Returns:
            int: El volumen actual del vúmetro
        """
        return self.volume_level

    def set_lcd_calibration_db(self, calibration_db: int):
        """Cambia el factor de escala que se usa para normalizar el volumen

        Esto sirve para calibrar el micrófono y que el valor calculado se aproxime lo máximo posible al real

        Args:
            calibration_db (int): Factor de escala que se le quiere aplicar al audio captado por el micrófono
        """
        if calibration_db < 1:
            calibration_db = 1
        self.calibration_db = calibration_db

    def set_max_calibration_range(self, max_detection_range: int):
        """Cambia rango máximo de volumen que se quiere representar gráficamente en el vúmetro

        Esto sirve para calibrar el vúmetro y que muestre el rango de volumen que se desee, apreciando más o menos detalle en la variación de volumen en la representación grafica.

        Args:
            max_detection_range (int): Range máximo de volumen que se quiere representar gráficamente en el vúmetro
        """
        if max_detection_range < 1:
            max_detection_range = 1
        self.detection_range = max_detection_range

    def set_background_color(self, color: str):
        """Cambia el color de fondo del vúmetro

        El método recibe un String con el color en formato hexadecimal y lo establece como el color de fondo del vúmetro

        En caso de que el String no sea un color valido, no se hace ningún cambio

        Args:
            color (str): Color en formato hexadecimal
        """
        if not re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            return
        self.background_color = color
        self.configuration_update = True
        self.update()

    def set_bars_color(self, color: str):
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
        self.bars_color = array_color
        self.configuration_update = True
        self.update()

    def set_max_elements(self, elements: int):
        """Recibe el número de máximo elementos que se quieren mostrar en el vúmetro

        En el caso del estilo vúmetro barras, este número indica el número máximo de barras que se quieren mostrar

        Args:
            elements (int): número de elementos que representan el volumen
        """
        if elements < 1:
            elements = 1
        self.num_bars = elements
        self.volume_spectrum = [0] * elements
        self.configuration_update = True
        self.update()

    def set_solid_percentage(self, percent: float):
        '''Cambia el porcentaje de espacio entre barras

        Este método recibe un numero entre 0 y 1 que indica el porcentaje de espacio que se quiere entre las barras del vúmetro

        Args:
            percent (float): Porcentaje de espacio entre barras
        '''
        if percent < 0.1:
            percent = 0.1
        elif percent > 0.9:
            percent = 0.9
        self.bars_solid_percentage = percent
        self.configuration_update = True
        self.update()

    def set_bars_direction(self, direction: VUMeterBarsDirection):
        '''Cambia la dirección del vúmetro en los estilos que permiten esta configuración

        Este método recibe un objeto de la clase VUMeterBarsDirection que indica la dirección que desde donde parte la representación grafica del audio

        Args:
            direction (VUMeterBarsDirection): Dirección del vúmetro
        '''
        self.bars_direction = direction.value
        self.configuration_update = True
        self.update()

    def set_min_detection_level(self, min_detection_level: int):
        '''Cambia el valor mínimo de detección del vúmetro

        Cambia el valor mínimo de detección del vúmetro, es decir, el valor mínimo que se quiere que se represente gráficamente

        Args:
            min_detection_level (int): Valor mínimo de detección del vúmetro
        '''
        if min_detection_level < 0:
            min_detection_level = 0

        self.min_detection_level = min_detection_level
        self.configuration_update = True
        self.update()

    def set_detection_speed(self, speed: int):
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
        self.INPUT_FRAMES_PER_BLOCK = int(self.SAMPLE_RATE * self.INPUT_BLOCK_TIME)

    def activate_vu_meter(self):
        '''Activa el vúmetro.

        Si el vúmetro no está ya activo, inicia un nuevo hilo que ejecuta el método _start_audio_capture del vúmetro
        '''
        if not self.vu_meter_on:
            hilo_vumetro = threading.Thread(target=self._start_audio_capture)
            hilo_vumetro.start()
            self.vu_meter_on = True

    def deactivate_vu_meter(self):
        '''Detiene el vúmetro

        Establece la variable vu_meter_on a False para que el hilo que ejecuta el método _start_audio_capture del vúmetro termine
        '''
        self.vu_meter_on = False

    def change_vu_meter_style(self, style: VUMeterStyle):
        '''Cambia el estilo del vúmetro

        Este método recibe un objeto de la clase VUMeterStyle que indica el estilo que se quiere para el vúmetro

        Args:
            style (VUMeterStyle): Estilo que se quiere para el vúmetro
        '''
        self.vu_meter_style = style.value
        self.update()

    def paintEvent(self, e):
        '''Método sobrescrito de QWidget para actualizar la representación gráfica del vúmetro

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

        if self.volume_level > self.max_detection_range:
            volumen_con_tope = self.max_detection_range
        else:
            volumen_con_tope = self.volume_level

        if (self.max_detection_range <= self.min_detection_level or self.volume_level <= self.min_detection_level) and self.vu_meter_style != 2:
            # painter.end()
            return

        if self.max_detection_range <= self.min_detection_level or self.volume_level < self.min_detection_level:
            volumen_con_tope = self.min_detection_level

        volumen_normalizado = (volumen_con_tope - self.min_detection_level) / \
            (self.max_detection_range - self.min_detection_level)
        num_elements_to_draw = int(volumen_normalizado * self.num_bars)

        # dimensiones del lienzo
        d_height = painter.device().height() - (self.bars_padding * 2)
        d_width = painter.device().width() - (self.bars_padding * 2)

        if self.vu_meter_style == 0:
            self._paint_bars(painter, d_height, d_width, num_elements_to_draw, brush)
        elif self.vu_meter_style == 1:
            self._paint_circles(painter, d_height, d_width, num_elements_to_draw)
        elif self.vu_meter_style == 2:
            self._paint_spectrum(painter, d_height, d_width, brush, volumen_normalizado)
        elif self.vu_meter_style == 3:
            self._paint_angle(painter, d_height, d_width, volumen_normalizado)

        painter.end()

    def _calculate_volume(self, audio_data):
        '''Método que calcula el volumen del audio captado por el micrófono

        Args:
            audio_data (bytes): Datos de audio captados por el micrófono
        '''
        NORMALIZE_FACTOR = 1.0 / 32768.0
        num_samples = len(audio_data) / 2
        audio_samples = struct.unpack("%dh" %num_samples, audio_data)
        sum_of_squares = sum((s * NORMALIZE_FACTOR) ** 2 for s in audio_samples)
        return math.sqrt(sum_of_squares / num_samples)

    def _start_audio_capture(self):
        '''Método que se ejecuta en un hilo para captar el audio del micrófono y calcular el volumen

        Este método se ejecuta en un hilo para que no bloquee la interfaz gráfica y pueda seguir funcionando mientras se captura el audio del micrófono y se calcula el volumen

        El método usa la librería PyAudio para captar el audio del micrófono y la clase Amplitude para calcular el volumen del audio captado

        El volumen calculado se asigna al QLCDNumber self.lcd_volume y se actualiza la representación gráfica del audio en el vúmetro

        El método termina cuando la variable vu_meter_on es False

        Llama a la función update para actualizar la representación gráfica del audio en el vúmetro
        '''
        audio = pyaudio.PyAudio()
        try:

            stream = audio.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=self.SAMPLE_RATE,
                                input=True,
                                frames_per_buffer=self.INPUT_FRAMES_PER_BLOCK,
                                )

            max_amplitude  = 0
            while True:
                if not self.vu_meter_on:
                    return

                try:
                    audio_data = stream.read(self.INPUT_FRAMES_PER_BLOCK)

                    current_amplitude = self._calculate_volume(audio_data)

                    if current_amplitude > max_amplitude :
                        max_amplitude  = current_amplitude

                    self.volume_level = int(current_amplitude * self.calibration_db)
                    print(self.volume_level)
                    self.lcd_volume.display(self.volume_level)
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

    def _paint_bars(self, painter: QPainter, d_height: int, d_width: int, num_elements_to_draw: int, brush: QBrush):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de barras

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de barras y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            num_elements_to_draw (int): Numero de barras que se quieren pintar
            brush (QBrush): Pincel que se usa para pintar la representación gráfica del audio en el vúmetro
        '''
        # divisiones del lienzo
        step_size_vertical = d_height / self.num_bars
        setp_size_horizontal = d_width / self.num_bars
        # alto barras
        bar_height_vertical = step_size_vertical * self.bars_solid_percentage
        bar_height_horizontal = setp_size_horizontal * self.bars_solid_percentage
        # Espacio entre barras
        bar_spacer_vertical = (step_size_vertical - bar_height_vertical) / 2
        bar_spacer_horizontal = (
            setp_size_horizontal - bar_height_horizontal) / 2

        for n in range(num_elements_to_draw):
            nextColor = (int)(n // (self.num_bars / len(self.bars_color)))
            # Un color por barra
            brush.setColor(QColor(self.bars_color[nextColor]))
            if self.bars_direction == 0:
                rect = QRect(
                    self.bars_padding,
                    self.bars_padding + d_height -
                    ((n+1) * step_size_vertical) + bar_spacer_vertical,
                    d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 1:
                rect = QRect(
                    self.bars_padding + (n * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    self.bars_padding,
                    bar_height_horizontal,
                    d_height
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 2:
                rect = QRect(
                    self.bars_padding,
                    self.bars_padding + (n * step_size_vertical) +
                    bar_spacer_vertical,
                    d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 3:
                rect = QRect(
                    self.bars_padding + d_width -
                    ((n+1) * setp_size_horizontal) + bar_spacer_horizontal,
                    self.bars_padding,
                    bar_height_horizontal,
                    d_height
                )
                painter.fillRect(rect, brush)

    def _paint_circles(self, painter: QPainter, d_height: int, d_width: int, num_elements_to_draw: int):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de círculos

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de círculos y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            num_elements_to_draw (int): Numero de círculos que se quieren pintar
        '''
        diametroMax = min(d_height, d_width) - 2 * self.bars_padding
        step_size = (diametroMax/2) / self.num_bars
        width_pen = step_size * self.bars_solid_percentage
        width_spacer = step_size - width_pen
        pen = QPen()
        pen.setWidth(width_pen)
        centroX = d_width / 2 + 2 * self.bars_padding
        centroY = d_height / 2 + 2 * self.bars_padding

        for n in range(num_elements_to_draw):
            nextColor = (int)(n // (self.num_bars / len(self.bars_color)))
            pen.setColor(QColor(self.bars_color[nextColor]))
            painter.setPen(pen)
            painter.drawEllipse(
                centroX - (n+1) * width_pen - n * width_spacer,
                centroY - (n+1) * width_pen - n * width_spacer,
                (2*n+1) * width_pen + (2*n) * width_spacer,
                (2*n+1) * width_pen + (2*n) * width_spacer
            )

    def _paint_spectrum(self, painter: QPainter, d_height: int, d_width: int, brush: QBrush, volumen_normalizado: float):
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
        step_size_vertical = d_height / self.num_bars
        setp_size_horizontal = d_width / self.num_bars
        # alto barras
        bar_height_vertical = step_size_vertical * self.bars_solid_percentage
        bar_height_horizontal = setp_size_horizontal * self.bars_solid_percentage
        # Espacio entre barras
        bar_spacer_vertical = (step_size_vertical - bar_height_vertical) / 2
        bar_spacer_horizontal = (
            setp_size_horizontal - bar_height_horizontal) / 2

        centroX = d_width / 2
        centroY = d_height / 2
        if not self.configuration_update:
            self.volume_spectrum.pop(0)
            self.volume_spectrum.append(volumen_normalizado+0.01)
        self.configuration_update = False

        for n in range(len(self.volume_spectrum)):
            nextColor = (int)(n // (self.num_bars / len(self.bars_color)))
            # Un color por barra
            brush.setColor(QColor(self.bars_color[nextColor]))
            if self.bars_direction == 0:
                rect = QRect(
                    centroX - (self.volume_spectrum[n] * centroX),
                    self.bars_padding +
                    (n * step_size_vertical) + bar_spacer_vertical,
                    self.volume_spectrum[n] * d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 1:
                rect = QRect(
                    self.bars_padding + d_width - ((n+1) * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    centroY - (self.volume_spectrum[n] * centroY),
                    bar_height_horizontal,
                    self.volume_spectrum[n] * d_height
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 2:
                rect = QRect(
                    centroX - (self.volume_spectrum[n] * centroX),
                    self.bars_padding + d_height -
                    ((n+1) * step_size_vertical) + bar_spacer_vertical,
                    self.volume_spectrum[n] * d_width,
                    bar_height_vertical
                )
                painter.fillRect(rect, brush)
            elif self.bars_direction == 3:
                rect = QRect(
                    self.bars_padding + (n * setp_size_horizontal) +
                    bar_spacer_horizontal,
                    centroY - (self.volume_spectrum[n] * centroY),
                    bar_height_horizontal,
                    self.volume_spectrum[n] * d_height
                )
                painter.fillRect(rect, brush)

    def _paint_angle(self, painter: QPainter, d_height: int, d_width: int, volumen_normalizado: float):
        '''Pinta la representación gráfica del audio en el vúmetro según el estilo de ángulo

        Este método pinta la representación gráfica del audio en el vúmetro según el estilo de ángulo y las variables de configuración del vúmetro que se hayan elegido

        Args:
            painter (QPainter): Objeto que se usa para pintar la representación gráfica del audio en el vúmetro
            d_height (int): Altura del lienzo
            d_width (int): Ancho del lienzo
            volumen_normalizado (float): Volumen a mostrar escalado entre cero y uno
            '''
        diametroMax = min(d_height, d_width) - 2 * self.bars_padding
        center = QPoint(d_width / 2 + self.bars_padding,
                        d_height / 2 + self.bars_padding)
        boundingRect = QRectF(d_width / 2 + self.bars_padding - diametroMax / 2, d_height / 2 + self.bars_padding - diametroMax / 2, diametroMax, diametroMax)
        startAngle = 0
        finalAngle = volumen_normalizado * 360
        sweepLength = 360 / self.num_bars
        cantidad_pintado = int(finalAngle / sweepLength)

        for i in range(cantidad_pintado):
            nextColor = (int)(i // (self.num_bars / len(self.bars_color)))
            if nextColor >= len(self.bars_color):
                break
            painter.setPen(QPen(self.bars_color[nextColor]))
            myPath = QPainterPath()
            myPath.moveTo(center)
            myPath.arcTo(boundingRect, startAngle +
                         i * sweepLength, sweepLength)

            myGradient = QLinearGradient(0, 0, self.width(), self.height())
            myGradient.setColorAt(0.0, QColor(self.bars_color[nextColor]))
            myGradient.setColorAt(1.0, QColor(self.bars_color[nextColor]))

            painter.setBrush(myGradient)
            painter.drawPath(myPath)
