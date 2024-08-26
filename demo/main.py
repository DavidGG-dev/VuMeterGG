'''Programa para probar el widget VuMeterGG de manera grafica y poder ver todas sus posibiliades de configuracion'''

from PySide6.QtWidgets import QApplication, QWidget
from view.qt_ui.main_ui import Ui_Form

    
class MyForm(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        '''Inicializa el formulario y conecta los eventos de los widgets con los metodos correspondientes del widget VuMeterGG. Tambien agrega el widget lcd_volume al layout_lcd del formulario.'''
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.vumetro.show()
        self.pushB_start.clicked.connect(self.vumetro.activate_vu_meter)
        self.pushB_stop.clicked.connect(self.vumetro.deactivate_vu_meter)
        self.layout_lcd.addWidget(self.vumetro.lcd_volume)
        self.dial_calibrarDB.valueChanged.connect(self.calibrarDB)
        self.dial_calibrarRango.valueChanged.connect(self.calibrarRango)

        # color fondo del lienzo
        self.radioB_backgroundBlack.toggled.connect(
            lambda: self.vumetro.set_background_color('#000000'))
        self.radioB_backgroundGrey.toggled.connect(
            lambda: self.vumetro.set_background_color('#282a36'))
        self.radioB_backgroundWhite.toggled.connect(
            lambda: self.vumetro.set_background_color('#FFFFFF'))
        self.radioB_backgroundCustom.toggled.connect(
            lambda: self.vumetro.set_background_color(self.lineE_backgroundCustomColor.text()))
        self.lineE_backgroundCustomColor.textChanged.connect(
            self.changeColorBackgroundCustom)

        # color barra
        self.radioB_barColorAzul.toggled.connect(
            lambda: self.vumetro.set_bars_color('#00BFFF'))
        self.radioB_barColorRosa.toggled.connect(
            lambda: self.vumetro.set_bars_color('#FF1493'))
        self.radioB_barColorMoradoCascada.toggled.connect(
            lambda: self.vumetro.set_bars_color('#49006a,#7a0177,#ae017e,#dd3497,#f768a1,#fa9fb5,#fcc5c0,#fde0dd,#fff7f3'))
        self.radioB_barColorArcoirisCascada.toggled.connect(
            lambda: self.vumetro.set_bars_color("#5A07EB,#0726EB,#086EEA,#07B5EB, #07EBD7,#00EAB4,#00EB7D,#01EB3F,#2BEB00,#8FEB09,#B4EB00,#EBDE00, #EBC200, #EBA500, #EB9A01,#EB7600,#EB4D00,#EB2400"))
        self.radioB_barColorCustom.toggled.connect(
            lambda: self.vumetro.set_bars_color(self.plainT_barColorCustom.toPlainText()))
        self.plainT_barColorCustom.textChanged.connect(
            self.changeColorBarCustom)

        # Numero de barras
        self.spinB_nSteps.valueChanged.connect(
            lambda: self.vumetro.set_max_elements(self.spinB_nSteps.value()))
        # porcentaje de espacio entre barras
        self.doubleS_solidPercent.valueChanged.connect(
            lambda: self.vumetro.set_solid_percentage(
                self.doubleS_solidPercent.value()))

        # Direccion estilo barras
        self.radioB_dirrecionArriba.toggled.connect(
            lambda: self.vumetro.set_bars_direction(self.vumetro.VUMeterBarsDirection.UP))
        self.radioB_dirrecionAbajo.toggled.connect(
            lambda: self.vumetro.set_bars_direction(self.vumetro.VUMeterBarsDirection.DOWN))
        self.radioB_dirrecionDerecha.toggled.connect(
            lambda: self.vumetro.set_bars_direction(self.vumetro.VUMeterBarsDirection.RIGHT))
        self.radioB_dirrecionIzquierda.toggled.connect(
            lambda: self.vumetro.set_bars_direction(self.vumetro.VUMeterBarsDirection.LEFT))

        self.spinB_minDetection.valueChanged.connect(
            lambda: self.vumetro.set_min_detection_level(self.spinB_minDetection.value()))

        self.horizontalS_velocidad.valueChanged.connect(
            lambda: self.vumetro.set_detection_speed(self.horizontalS_velocidad.value()))

        # Estilo del vumetro
        self.radioB_estiloBarras.toggled.connect(self.changeEstiloBarras)
        self.radioB_estiloCirculos.toggled.connect(self.changeEstiloCirculos)
        self.radioB_estiloEspectro.toggled.connect(self.changeEstiloEspectro)
        self.radioB_estiloAngulo.toggled.connect(self.changeEstiloAngulo)

    def changeEstiloBarras(self):
        '''Cambia el estilo del vumetro a barras y habilita los radioButtons para seleccionar la direccion de las barras.'''
        self.vumetro.change_vu_meter_style(
            self.vumetro.VUMeterStyle.BARS)
        self.radioB_dirrecionAbajo.setEnabled(True)
        self.radioB_dirrecionArriba.setEnabled(True)
        self.radioB_dirrecionDerecha.setEnabled(True)
        self.radioB_dirrecionIzquierda.setEnabled(True)
        self.doubleS_solidPercent.setEnabled(True)

    def changeEstiloCirculos(self):
        '''Cambia el estilo del vumetro a circulos y deshabilita los radioButtons para seleccionar la direccion de las barras.'''
        self.vumetro.change_vu_meter_style(
            self.vumetro.VUMeterStyle.CIRCLES)
        self.radioB_dirrecionAbajo.setEnabled(False)
        self.radioB_dirrecionArriba.setEnabled(False)
        self.radioB_dirrecionDerecha.setEnabled(False)
        self.radioB_dirrecionIzquierda.setEnabled(False)
        self.doubleS_solidPercent.setEnabled(True)

    def changeEstiloAngulo(self):
        '''Cambia el estilo del vumetro a circulos y deshabilita los radioButtons para seleccionar la direccion de las barras.'''
        self.vumetro.change_vu_meter_style(
            self.vumetro.VUMeterStyle.ANGLE)
        self.radioB_dirrecionAbajo.setEnabled(False)
        self.radioB_dirrecionArriba.setEnabled(False)
        self.radioB_dirrecionDerecha.setEnabled(False)
        self.radioB_dirrecionIzquierda.setEnabled(False)
        self.doubleS_solidPercent.setEnabled(False)

    def changeEstiloEspectro(self):
        '''Cambia el estilo del vumetro a espectro y habilita los radioButtons para seleccionar la direccion de las barras.'''
        self.vumetro.change_vu_meter_style(
            self.vumetro.VUMeterStyle.SPECTRUM)
        self.radioB_dirrecionAbajo.setEnabled(True)
        self.radioB_dirrecionArriba.setEnabled(True)
        self.radioB_dirrecionDerecha.setEnabled(True)
        self.radioB_dirrecionIzquierda.setEnabled(True)
        self.doubleS_solidPercent.setEnabled(True)

    def changeColorBackgroundCustom(self):
        '''Cambia el color de fondo del lienzo del vumetro al color ingresado en el lineEdit lineE_backgroundCustomColor.'''
        if self.radioB_backgroundCustom.isChecked():
            self.vumetro.set_background_color(
                self.lineE_backgroundCustomColor.text())

    def changeColorBarCustom(self):
        '''Cambia el color de las barras del vumetro al color ingresado en el plainTextEdit plainT_barColorCustom.'''
        if self.radioB_barColorCustom.isChecked():
            self.vumetro.set_bars_color(
                self.plainT_barColorCustom.toPlainText())

    def calibrarDB(self):
        '''Cambia el valor de calibracion del vumetro en dB segun el valor del dial dial_calibrarDB. Tambien actualiza el valor en el lcd lcdN_calibrarDB.'''
        self.vumetro.set_lcd_calibration_db(self.dial_calibrarDB.value())
        self.lcdN_calibrarDB.display(self.dial_calibrarDB.value())

    def calibrarRango(self):
        '''Cambia el valor de calibracion del vumetro en rango segun el valor del dial dial_calibrarRango. Tambien actualiza el valor en el lcd lcdN_calibrarRango.'''
        self.vumetro.set_max_calibration_range(
            self.dial_calibrarRango.value())
        self.lcdN_calibrarRango.display(self.dial_calibrarRango.value())

    def closeEvent(self, event):
        '''Al cerrar el formulario se apaga el vumetro.'''
        self.vumetro.deactivate_vu_meter()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myform = MyForm()
    myform.show()
    sys.exit(app.exec())
