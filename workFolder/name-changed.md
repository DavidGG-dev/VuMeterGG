# replaced names

Temporary file to store recent changes in the names of variables and methods in the project. Useful as a reference for collaborators in case they need to consult it.

old name -> new name

## global variables

RATE -> SAMPLE_RATE

encendido -> vu_meter_on

estiloVumetro -> vu_meter_style

directionVumetroBarras -> bars_direction

number_bars -> num_bars

calibracion_db -> calibration_db

range_detection -> max_detection_range

volumen -> volume_level

espectroVolumen - > volume_spectrum

padding_barras -> bars_padding

solid_percent -> bars_solid_percentage

bar_color -> bars_color

actulizacionConfiguracion -> configuration_update

## Enum Classes

EstiloVumetro -> VUMeterStyle
- BARRAS -> BARS
- CIRCULOS -> CIRCLES
- ESPECTRO -> SPECTRUM
- ANGULO -> ANGLE

DirectionVumetroBarras -> VUMeterBarsDirection
- ARRIBA -> UP
- DERECHA -> RIGHT
- ABAJO -> DOWN
- IZQUIERDA -> LEFT

## Methods

activar_vumetro -> activate_vu_meter

desactivar_vumetro - > deactivate_vu_meter

get_volumen -> get_volume_level

set_vumeter_speed -> set_detection_speed

calculate_volume -> _calculate_volume

start_audio_capture -> _start_audio_capture

paintEvent -> _paint_event

setBackgroundColor -> set_background_color

setBarColor -> set_bars_color

setSolidPercent -> set_solid_percentage

setDirectionVumetroBarras -> set_bars_direction


set_lcd_calibrarDB -> set_lcd_calibration_db
- db -> calibration_db

set_lcd_calibrarRango -> set_max_calibration_range
- rango -> max_detection_range

setStep -> set_max_elements
- step -> elements

changeStyleVumetro -> change_vu_meter_style
- estilo -> style

setMinDetection -> set_min_detection_level
- minimal -> min_detection_level

pintar_barras -> paint_bars
- num_steps_to_draw -> num_elements_to_draw

pintar_circulos -> paint_circles
- num_steps_to_draw -> num_elements_to_draw

pintar_espectro -> paint_spectrum
- num_steps_to_draw -> num_elements_to_draw

pintar_angulo -> _paint_angle
- num_steps_to_draw -> num_elements_to_draw