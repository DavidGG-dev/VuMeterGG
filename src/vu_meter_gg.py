"""This module defines an audio VU meter widget for PySide6

The widget is used to graphically represent the audio levels
captured through a microphone in real time

This widget can be promoted and used in QtDesigner for PySide6

The widget has numerous configuration parameters among which are
those that modify the physical appearance and those that modify the
way of receiving the audio signal
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
    ''' Class representing the entire module

This class contains all the attributes and functions used
for the operation of the widget and that allow you to change its behavior

Args:
QWidget (QWidget): Class from which it inherits and that allows it to be used as a widget

Attributes:
SAMPLE_RATE (int): Audio sampling frequency
INPUT_BLOCK_TIME (float): Time taken to capture the audio
INPUT_FRAMES_PER_BLOCK (int): Number of frames captured in the INPUT_BLOCK_TIME time
vu_meter_on (bool): Indicates whether the vu meter is active
vu_meter_style (int): Indicates the desired vu meter style
bars_direction (int): Indicates the direction of the vu meter bars
num_bars (int): Number of bars to be displayed
calibration_db (int): Scale factor to be applied to the audio captured by the microphone
max_detection_range (int): Maximum volume range to be represented graphically in the VU meter
min_detection_level (int): Minimum detection value of the VU meter
volume_level (int): Current normalized volume of the VU meter
volume_spectrum (list of int): List that stores the volume spectrum
bars_padding (int): Space between the graphical representation of the audio and the edge of the canvas
bars_solid_percentage (float): Percentage of space between bars
background_color (str): Background color of the VU meter
bars_color (str): Color of the graphical representation of the audio
configuration_update (bool): Controls that the SPECTRUM style is updated correctly when changes are made to the configuration
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
        '''Enum class to choose the type of VU meter

Args:
Enum (Enum): Class from which it inherits to make an enum class with constants

Attributes:
BARS (int): Indicates that the VU meter style is bars
CIRCLES (int): Indicates that the VU meter style is circles
SPECTRUM (int): Indicates that the VU meter style is an audio spectrogram
ANGLE (int): Indicates that the VU meter style is angle
'''
        BARS = 0
        CIRCLES = 1
        SPECTRUM = 2
        ANGLE = 3

    class VUMeterBarsDirection(Enum):
      '''Enum class to choose the direction of the VU meter
Args:
Enum (Enum): Class from which it inherits to make an enum class with constants

Attributes:
UP (int): Indicates that the direction of the VU meter is upwards
RIGHT (int): Indicates that the direction of the VU meter is to the right
DOWN (int): Indicates that the direction of the VU meter is downwards
LEFT (int): Indicates that the direction of the VU meter is to the left
'''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    def __init__(self, *args, **kwargs):
        '''Calls two functions to create a QLCDNumber object and initializes the VU meter'''
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
        """Gets the current normalized volume of the VU meter

Returns:
int: The current volume of the VU meter
"""
        return self.volume_level

    def set_lcd_calibration_db(self, calibration_db: int):
       """Change the scale factor used to normalize the volume

This is used to calibrate the microphone so that the calculated value is as close as possible to the real value

Args:
calibration_db (int): Scale factor that you want to apply to the audio captured by the microphone
"""
        if calibration_db < 1:
            calibration_db = 1
        self.calibration_db = calibration_db

    def set_max_calibration_range(self, max_detection_range: int):
       """Change the maximum volume range that you want to represent graphically on the VU meter

This is used to calibrate the VU meter and display the desired volume range, showing more or less detail in the volume variation in the graphical representation.

Args:
max_detection_range (int): Maximum volume range that you want to represent graphically on the VU meter
"""
        if max_detection_range < 1:
            max_detection_range = 1
        self.detection_range = max_detection_range

    def set_background_color(self, color: str):
        """Change the background color of the VU meter

The method receives a String with the color in hexadecimal format and sets it as the background color of the VU meter

If the String is not a valid color, no change is made

Args:
color (str): Color in hexadecimal format
"""
        if not re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            return
        self.background_color = color
        self.configuration_update = True
        self.update()

    def set_bars_color(self, color: str):
        """Change the color of the VU meter

Changes the color of the graphical representation of the audio captured by the microphone

The method receives a String with one or more colors in hexadecimal format separated by commas and sets it as the color(s) used to represent the audio

If the String does not contain a valid color, no change is made

The color/colors are saved as an array of Strings with the colors in hexadecimal format

Args:
color (str): Color in hexadecimal format
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
        """Receives the maximum number of elements to be displayed in the VU meter

In the case of the bars VU meter style, this number indicates the maximum number of bars to be displayed

Args:
elements (int): number of elements representing the volume
"""
        if elements < 1:
            elements = 1
        self.num_bars = elements
        self.volume_spectrum = [0] * elements
        self.configuration_update = True
        self.update()

    def set_solid_percentage(self, percent: float):
        '''Change the percentage of space between bars

This method receives a number between 0 and 1 that indicates the percentage of space that is wanted between the bars of the VU meter

Args:
percent (float): Percentage of space between bars
'''
        if percent < 0.1:
            percent = 0.1
        elif percent > 0.9:
            percent = 0.9
        self.bars_solid_percentage = percent
        self.configuration_update = True
        self.update()

    def set_bars_direction(self, direction: VUMeterBarsDirection):
       '''Change the direction of the VUMeter in the styles that allow this configuration

This method receives an object of the VUMeterBarsDirection class that indicates the direction from which the graphical representation of the audio starts

Args:
direction (VUMeterBarsDirection): Direction of the VUMeter
'''
        self.bars_direction = direction.value
        self.configuration_update = True
        self.update()

    def set_min_detection_level(self, min_detection_level: int):
       '''Change the minimum detection value of the VU meter

Changes the minimum detection value of the VU meter, that is, the minimum value that you want to be represented graphically

Args:
min_detection_level (int): Minimum detection value of the VU meter
'''
        if min_detection_level < 0:
            min_detection_level = 0

        self.min_detection_level = min_detection_level
        self.configuration_update = True
        self.update()

    def set_detection_speed(self, speed: int):
        '''Change the VU meter detection speed

Changes the VU meter detection speed, i.e. the time it takes to update the graphical representation of the audio

Args:
speed (int): VU meter detection speed
'''
        if speed < 1:
            speed = 1
        elif speed > 25:
            speed = 25

        self.INPUT_BLOCK_TIME = float(speed) / 100
        self.INPUT_FRAMES_PER_BLOCK = int(self.SAMPLE_RATE * self.INPUT_BLOCK_TIME)

    def activate_vu_meter(self):
        '''Activates the VU meter.

If the VU meter is not already active, starts a new thread that executes the VU meter's _start_audio_capture method.
'''
        if not self.vu_meter_on:
            hilo_vumetro = threading.Thread(target=self._start_audio_capture)
            hilo_vumetro.start()
            self.vu_meter_on = True

    def deactivate_vu_meter(self):
       '''Stops the VU meter

Sets the vu_meter_on variable to False so that the thread executing the VU meter's _start_audio_capture method will terminate
'''
        self.vu_meter_on = False

    def change_vu_meter_style(self, style: VUMeterStyle):
        '''Change the style of the VUMeter

This method receives an object of the VUMeterStyle class that indicates the style that is desired for the VUMeter

Args:
style (VUMeterStyle): Style that is desired for the VUMeter
'''
        self.vu_meter_style = style.value
        self.update()

    def paintEvent(self, e):
       '''QWidget override method to update the VU meter graphical representation

The method paints the graphical representation of the audio on the VU meter according to the chosen style

Uses the VU meter configuration variables to paint the graphical representation of the audio according to the chosen style

Args:
e (QPaintEvent): Paint event
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

        # canvas dimensions
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
        '''Method that calculates the volume of the audio captured by the microphone

Args:
audio_data (bytes): Audio data captured by the microphone
'''
        NORMALIZE_FACTOR = 1.0 / 32768.0
        num_samples = len(audio_data) / 2
        audio_samples = struct.unpack("%dh" %num_samples, audio_data)
        sum_of_squares = sum((s * NORMALIZE_FACTOR) ** 2 for s in audio_samples)
        return math.sqrt(sum_of_squares / num_samples)

    def _start_audio_capture(self):
        '''Method that runs in a thread to capture microphone audio and calculate volume

This method runs in a thread so that it does not block the graphical interface and can continue to run while the microphone audio is being captured and the volume is being calculated

The method uses the PyAudio library to capture microphone audio and the Amplitude class to calculate the volume of the captured audio

The calculated volume is assigned to the QLCDNumber self.lcd_volume and the graphical representation of the audio in the vu meter is updated

The method ends when the vu_meter_on variable is False

Calls the update function to update the graphical representation of the audio in the vu meter
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
                    print(f"Error reading audio: {e}")
                    continue

        except Exception as e:
            print(f"Error opening audio stream: {e}")

        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()

    def _paint_bars(self, painter: QPainter, d_height: int, d_width: int, num_elements_to_draw: int, brush: QBrush):
       '''Paints the graphical representation of the audio on the VU meter according to the bar style

This method paints the graphical representation of the audio on the VU meter according to the bar style and the VU meter configuration variables that have been chosen

Args:
painter (QPainter): Object used to paint the graphical representation of the audio on the VU meter
d_height (int): Height of the canvas
d_width (int): Width of the canvas
num_elements_to_draw (int): Number of bars to be painted
brush (QBrush): Brush used to paint the graphical representation of the audio on the VU meter
'''
        # canvas divisions
        step_size_vertical = d_height / self.num_bars
        setp_size_horizontal = d_width / self.num_bars
        # high bars
        bar_height_vertical = step_size_vertical * self.bars_solid_percentage
        bar_height_horizontal = setp_size_horizontal * self.bars_solid_percentage
        # Space between bars
        bar_spacer_vertical = (step_size_vertical - bar_height_vertical) / 2
        bar_spacer_horizontal = (
            setp_size_horizontal - bar_height_horizontal) / 2

        for n in range(num_elements_to_draw):
            nextColor = (int)(n // (self.num_bars / len(self.bars_color)))
            # One color per bar
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
'''Paints the graphical representation of the audio on the VU meter according to the circle style

This method paints the graphical representation of the audio on the VU meter according to the circle style and the VU meter configuration variables that have been chosen

Args:
painter (QPainter): Object used to paint the graphical representation of the audio on the VU meter
d_height (int): Height of the canvas
d_width (int): Width of the canvas
num_elements_to_draw (int): Number of circles to be painted
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
        '''Paints the graphical representation of the audio on the VU meter according to the spectrum style

This method paints the graphical representation of the audio on the VU meter according to the spectrum style and the VU meter configuration variables that have been chosen

Args:
painter (QPainter): Object used to paint the graphical representation of the audio on the VU meter
d_height (int): Height of the canvas
d_width (int): Width of the canvas
brush (QBrush): Brush used to paint the graphical representation of the audio on the VU meter
normalized_volume (float): Volume to display scaled between zero and one
'''
        # canvas divisions
        step_size_vertical = d_height / self.num_bars
        setp_size_horizontal = d_width / self.num_bars
        # alto barras
        bar_height_vertical = step_size_vertical * self.bars_solid_percentage
        bar_height_horizontal = setp_size_horizontal * self.bars_solid_percentage
        # Space between bars
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
            # One color per bar
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
       '''Paints the graphical representation of the audio on the VU meter according to the angle style

This method paints the graphical representation of the audio on the VU meter according to the angle style and the VU meter configuration variables that have been chosen

Args:
painter (QPainter): Object used to paint the graphical representation of the audio on the VU meter
d_height (int): Height of the canvas
d_width (int): Width of the canvas
normalized_volume (float): Volume to display scaled between zero and one
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
