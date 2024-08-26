# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from view.qt_ui.promoted.vu_meter_gg import VUMeterGG
import darkstyle_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(917, 604)
        Form.setMinimumSize(QSize(500, 0))
        Form.setStyleSheet(u"/* ---------------------------------------------------------------------------\n"
"\n"
"    WARNING! File created programmatically. All changes made in this file will be lost!\n"
"\n"
"    Created by the qtsass compiler v0.4.0\n"
"\n"
"    The definitions are in the \"qdarkstyle.qss._styles.scss\" module\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* Light Style - QDarkStyleSheet ------------------------------------------ */\n"
"/*\n"
"\n"
"See Qt documentation:\n"
"\n"
"  - https://doc.qt.io/qt-5/stylesheet.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* Reset elements ------------------------------------------------------------\n"
"\n"
"Resetting everything helps to unify styles across different operating systems\n"
"\n"
"--------------------------------------------------------------------------- */"
                        "\n"
"* {\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border: 0px;\n"
"  border-style: none;\n"
"  border-image: none;\n"
"  outline: 0;\n"
"}\n"
"\n"
"/* specific reset for elements inside QToolBar */\n"
"QToolBar * {\n"
"  margin: 0px;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"/* QWidget ----------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 0px;\n"
"  color: #DFE1E2;\n"
"  selection-background-color: #346792;\n"
"  selection-color: #DFE1E2;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"  selection-background-color: #26486B;\n"
"  selection-color: #788D9C;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QWidget::item:hover:!selected {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"/* QMainWindow --------------------------------------------"
                        "----------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #60798B;\n"
"  border: 0px solid #1A72BB;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/icons/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/icons/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolti"
                        "p\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #346792;\n"
"  color: #DFE1E2;\n"
"  /* If you remove the border property, background stops working on Windows */\n"
"  border: none;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Remove opacity, fix #174 - may need to use RGBA */\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #455364;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #455364;\n"
"  /* Fixes #205, white vertical borders separating items */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #1A72BB;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Re"
                        "move padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/icons/checkbox_unchecked.png\");\n"
"}\n"
"\n"
""
                        "QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/icons/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/icons/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/icons/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/icons/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  image: url(\":/icons/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:fo"
                        "cus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/icons/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  margin-top: 6px;\n"
"  margin-bottom: 4px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 4px;\n"
"  padding-left: 2px;\n"
"  padding-right: 4px;\n"
"  padding-top: -4px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  margin-top: 2px;\n"
"  padding: 0;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox"
                        "_unchecked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(\":/icons/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_checked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/icons/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"------------------------------------------------------"
                        "--------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 4px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/icons/radio_unchecked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":"
                        "/icons/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/icons/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #455364;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
""
                        "  color: #DFE1E2;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"  color: #DFE1E2;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #455364;\n"
"  color: #DFE1E2;\n"
"  margin: 0px;\n"
"  background-color: #37414F;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  h"
                        "eight: 1px;\n"
"  background-color: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #37414F;\n"
"  padding: 4px 24px 4px 28px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #DFE1E2;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  padding-left: 10px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  padding-left: 8px;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/icons/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:hover, QMenu::indicator:non-exclusive:unchecked:focus, QMenu"
                        "::indicator:non-exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:disabled {\n"
"  image: url(\":/icons/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/icons/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:hover, QMenu::indicator:non-exclusive:checked:focus, QMenu::indicator:non-exclusive:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/icons/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:disabled {\n"
"  image: url(\":/icons/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate {\n"
"  image: url(\":/icons/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate:disabled {\n"
"  image: url(\":/icons/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusi"
                        "ve:indeterminate:focus, QMenu::indicator:non-exclusive:indeterminate:hover, QMenu::indicator:non-exclusive:indeterminate:pressed {\n"
"  image: url(\":/icons/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/icons/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:hover, QMenu::indicator:exclusive:unchecked:focus, QMenu::indicator:exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:disabled {\n"
"  image: url(\":/icons/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:hover, QMenu::indicator:exclusive:checked:focus, QMenu::indicator:exclusive:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/icons/"
                        "radio_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/icons/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  padding-left: 12px;\n"
"  image: url(\":/icons/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"------------------------------"
                        "--------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* fix #159 */\n"
"  padding: 2px;\n"
"  /* remove min-height to fix #244 */\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D"
                        ";\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::add-line:ho"
                        "rizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/icons/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/icons/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/icons/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/icons/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3p"
                        "x 0px 3px;\n"
"  border-image: url(\":/icons/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/icons/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/icons/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/icons/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
""
                        "\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- *"
                        "/\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/icons/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #455364;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar -----------------------"
                        "----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #455364;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 1px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar:disabled {\n"
"  /* Fixes #272 */\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/icons/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/icons/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/icons/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/icons/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #45"
                        "5364;\n"
"  border: 0px;\n"
"  color: #DFE1E2;\n"
"  image: url(\":/icons/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #455364;\n"
"  border-bottom: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-bottom: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBo"
                        "x::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/icons/arrow_up_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/icons/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #455364;\n"
"  border-top: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-top: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/icons/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #346792;\n"
" "
                        " color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractSpinBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------"
                        "------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455"
                        "364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet"
                        "-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #346792;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #26486B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton -----------------------------------"
                        "-------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #60798B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #60798B;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #6"
                        "0798B;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"  /* Issue #194 #248 - Special case of QPushButton inside dialogs, for better UI */\n"
"  min-width: 80px;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"  border: none;\n"
"  /* The subcontrols below are used only in the DelayedPopup mode */\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or "
                        "DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  background-color: #60798B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:checked:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:checked:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"0\""
                        "] {\n"
"  /* Only for DelayedPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 20px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button:hover {\n"
"  border: none;\n"
"  border-left: 1px solid #455364;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  width: 12px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"  top: 0;\n"
"  /* Exclude a shift for better image */\n"
"  left: -2"
                        "px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:hover {\n"
"  image: url(\":/icons/arrow_down_focus.png\");\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox -----------------------------"
                        "---------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #346792;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  /* padding-right = 36; 4 + 16*2 See scrollbar size */\n"
"  /* changed to 4px to fix #239 */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 0;\n"
"  background-color: #19232D;\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:hover {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"}\n"
""
                        "\n"
"QComboBox QAbstractItemView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  border: none;\n"
"  border-radius: 0;\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"  /* Remove to fix #282, #285 and MR #288*/\n"
"  /*&:checked {\n"
"            font-weight: bold;\n"
"        }\n"
"\n"
"        &:selected {\n"
"            borde"
                        "r: 0px solid transparent;\n"
"        }\n"
"        */\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/icons/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #455364;\n"
"  border: 1px solid #455"
                        "364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #455364;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: #346792;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #346792;\n"
"  border: 1px solid #455364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #346792;\n"
"  border: 1px solid"
                        " #346792;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #346792;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QSlider::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #455364;\n"
" "
                        " border-radius: 4px;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #455364;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidg"
                        "et::pane:selected {\n"
"  background-color: #455364;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar, QDockWidget QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button, QDockWidget QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 4px;\n"
"  image: url(\":/icons/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover, QDockWidget QTabBar::close-button:hover {\n"
"  image: url(\":/icons/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed, QDockWidget QTabBar::close-button:pressed {\n"
"  image: url(\":/icons/window_close_pressed.pn"
                        "g\");\n"
"}\n"
"\n"
"QTabBar::tab, QDockWidget QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled, QDockWidget QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled, QDockWidget QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled, QDockWidget QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled, QDockWidget QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar:"
                        ":tab:top:!selected:disabled, QDockWidget QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled, QDockWidget QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled, QDockWidget QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled, QDockWidget QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected, QDockWidget QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected, QDockWidget QTabBar::tab:bottom:!selected {\n"
"  border-top:"
                        " 2px solid #19232D;\n"
"  margin-bottom: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected, QDockWidget QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected, QDockWidget QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QDockWidget QTabBar::tab:top {\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #455364;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected, QDockWidget QTabBar::tab:top:selected {\n"
"  background-color: #54687A;\n"
"  border-bottom: 3px solid #259AE9;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover, QDockWidget QTabBar::tab:top:!selected:hover {\n"
""
                        "  border: 1px solid #1A72BB;\n"
"  border-bottom: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  padding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom, QDockWidget QTabBar::tab:bottom {\n"
"  border-top: 3px solid #455364;\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected, QDockWidget QTabBar::tab:bottom:selected {\n"
"  background-color: #54687A;\n"
"  border-top: 3px solid #259AE9;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover, QDockWidget QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-top: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  pa"
                        "dding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QDockWidget QTabBar::tab:left {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected, QDockWidget QTabBar::tab:left:selected {\n"
"  background-color: #54687A;\n"
"  border-right: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover, QDockWidget QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-right: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-right: 0px;\n"
"  padding-right: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:right, QDockWidget QTabBar::tab:right {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 4px;\n"
" "
                        " border-bottom-right-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected, QDockWidget QTabBar::tab:right:selected {\n"
"  background-color: #54687A;\n"
"  border-left: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover, QDockWidget QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-left: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-left: 0px;\n"
"  padding-left: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton, QDockWidget QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #455364;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed, QDockWidget QTabBar QToolButton:pressed {\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover, QDockWidget QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled, QDockWidget QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/ico"
                        "ns/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled, QDockWidget QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/icons/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled, QDockWidget QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/icons/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled, QDockWidget QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/icons/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #455364;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/icons/transparent.png\");\n"
"  titlebar-normal-icon: url(\":/icons/transparent.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for "
                        "title bar */\n"
"  padding: 3px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  icon-size: 12px;\n"
"  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/icons/window_close.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/icons/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/icons/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  icon-size: 12px;\n"
"  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/icons/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/icons/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/icons/window_undock_pres"
                        "sed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/icons/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/icons/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/icons/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/icons/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-ima"
                        "ge: none;\n"
"  image: url(\":/icons/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/icons/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/icons/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/icons/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked,\n"
"QTableView::indicator:checked,\n"
"QColumnView::indicator:checked {\n"
"  image: url(\":/icons/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
""
                        "QListView::indicator:checked:pressed,\n"
"QTableView::indicator:checked:hover,\n"
"QTableView::indicator:checked:focus,\n"
"QTableView::indicator:checked:pressed,\n"
"QColumnView::indicator:checked:hover,\n"
"QColumnView::indicator:checked:focus,\n"
"QColumnView::indicator:checked:pressed {\n"
"  image: url(\":/icons/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked,\n"
"QTableView::indicator:unchecked,\n"
"QColumnView::indicator:unchecked {\n"
"  image: url(\":/icons/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed,\n"
"QTableView::indicator:unchecked:hover,\n"
"QTableView::indicator:unchecked:focus,\n"
"QTableView::indicator:unchecked:pressed,\n"
"QColumnView::indicator:unchecked:hover,\n"
"QColumnView::indicator:u"
                        "nchecked:focus,\n"
"QColumnView::indicator:unchecked:pressed {\n"
"  image: url(\":/icons/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate,\n"
"QTableView::indicator:indeterminate,\n"
"QColumnView::indicator:indeterminate {\n"
"  image: url(\":/icons/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed,\n"
"QTableView::indicator:indeterminate:hover,\n"
"QTableView::indicator:indeterminate:focus,\n"
"QTableView::indicator:indeterminate:pressed,\n"
"QColumnView::indicator:indeterminate:hover,\n"
"QColumnView::indicator:indeterminate:focus,\n"
"QColumnView::indicator:indeterminate:pressed {\n"
"  image: url(\":/icons/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QL"
                        "istView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  gridline-color: #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QTreeView:focus,\n"
"QListView:focus,\n"
"QTableView:focus,\n"
"QColumnView:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
""
                        "QTreeView::item:selected:!active,\n"
"QListView::item:selected:!active,\n"
"QTableView::item:selected:!active,\n"
"QColumnView::item:selected:!active {\n"
"  color: #DFE1E2;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #DFE1E2;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #455364;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #455364;\n"
"  border: 0px transparent #455364;\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QHeaderView:dis"
                        "abled {\n"
"  background-color: #455364;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 0;\n"
"  text-align: left;\n"
"  font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #455364;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
""
                        "  color: #788D9C;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/icons/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QToolBox:selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #34"
                        "6792;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #60798B;\n"
"  border-bottom: 2px solid #346792;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #26486B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #455364;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #1A72BB;\n"
"  border-bottom: 2px solid #1A72BB;\n"
"}\n"
"\n"
"QToolBox QScrollArea {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/q"
                        "t-5/stylesheet-examples.html#customizing-qframe\n"
"https://doc.qt.io/qt-5/qframe.html#-prop\n"
"https://doc.qt.io/qt-5/qframe.html#details\n"
"https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* (dot) .QFrame  fix #141, #126, #123 */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  /* No frame */\n"
"  /* HLine */\n"
"  /* HLine */\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"4\"] {\n"
"  max-height: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"5\"] {\n"
"  max-width: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"------------"
                        "--------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #455364;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"  background-color: #9DA9B5;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/icons/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/icons/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit, QDateTimeEdit {\n"
"  selection-background-color: #346792;\n"
"  border-style: solid;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top:"
                        " 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on, QDateTimeEdit:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"  image: url(\":/icons/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
"  image: url(\":/icons/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  selection-background-color"
                        ": #346792;\n"
"}\n"
"\n"
"/* QAbstractView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractView:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* PlotWidget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 8, -1)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vumetro = VUMeterGG(self.frame_2)
        self.vumetro.setObjectName(u"vumetro")

        self.verticalLayout.addWidget(self.vumetro)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(340, 0))
        self.frame_4.setMaximumSize(QSize(350, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 460))
        self.frame_5.setMaximumSize(QSize(350, 460))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 220, 111, 151))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.radioB_backgroundBlack = QRadioButton(self.frame_7)
        self.radioB_backgroundBlack.setObjectName(u"radioB_backgroundBlack")
        self.radioB_backgroundBlack.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioB_backgroundBlack)

        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.radioB_backgroundGrey = QRadioButton(self.frame_7)
        self.radioB_backgroundGrey.setObjectName(u"radioB_backgroundGrey")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioB_backgroundGrey)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.radioB_backgroundWhite = QRadioButton(self.frame_7)
        self.radioB_backgroundWhite.setObjectName(u"radioB_backgroundWhite")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioB_backgroundWhite)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.radioB_backgroundCustom = QRadioButton(self.frame_7)
        self.radioB_backgroundCustom.setObjectName(u"radioB_backgroundCustom")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.radioB_backgroundCustom)

        self.lineE_backgroundCustomColor = QLineEdit(self.frame_7)
        self.lineE_backgroundCustomColor.setObjectName(u"lineE_backgroundCustomColor")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineE_backgroundCustomColor)


        self.verticalLayout_7.addLayout(self.formLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(120, 150, 225, 221))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.radioB_barColorAzul = QRadioButton(self.frame_8)
        self.radioB_barColorAzul.setObjectName(u"radioB_barColorAzul")
        self.radioB_barColorAzul.setChecked(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.radioB_barColorAzul)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_5)

        self.radioB_barColorRosa = QRadioButton(self.frame_8)
        self.radioB_barColorRosa.setObjectName(u"radioB_barColorRosa")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.radioB_barColorRosa)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_6)

        self.radioB_barColorMoradoCascada = QRadioButton(self.frame_8)
        self.radioB_barColorMoradoCascada.setObjectName(u"radioB_barColorMoradoCascada")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.radioB_barColorMoradoCascada)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_7)

        self.radioB_barColorArcoirisCascada = QRadioButton(self.frame_8)
        self.radioB_barColorArcoirisCascada.setObjectName(u"radioB_barColorArcoirisCascada")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.radioB_barColorArcoirisCascada)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_8)

        self.radioB_barColorCustom = QRadioButton(self.frame_8)
        self.radioB_barColorCustom.setObjectName(u"radioB_barColorCustom")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.radioB_barColorCustom)

        self.plainT_barColorCustom = QPlainTextEdit(self.frame_8)
        self.plainT_barColorCustom.setObjectName(u"plainT_barColorCustom")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.plainT_barColorCustom)


        self.verticalLayout_8.addLayout(self.formLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(250, 0, 95, 141))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_13.addWidget(self.label_16)

        self.radioB_dirrecionArriba = QRadioButton(self.frame_9)
        self.radioB_dirrecionArriba.setObjectName(u"radioB_dirrecionArriba")
        self.radioB_dirrecionArriba.setChecked(True)

        self.verticalLayout_13.addWidget(self.radioB_dirrecionArriba)

        self.radioB_dirrecionDerecha = QRadioButton(self.frame_9)
        self.radioB_dirrecionDerecha.setObjectName(u"radioB_dirrecionDerecha")

        self.verticalLayout_13.addWidget(self.radioB_dirrecionDerecha)

        self.radioB_dirrecionAbajo = QRadioButton(self.frame_9)
        self.radioB_dirrecionAbajo.setObjectName(u"radioB_dirrecionAbajo")

        self.verticalLayout_13.addWidget(self.radioB_dirrecionAbajo)

        self.radioB_dirrecionIzquierda = QRadioButton(self.frame_9)
        self.radioB_dirrecionIzquierda.setObjectName(u"radioB_dirrecionIzquierda")

        self.verticalLayout_13.addWidget(self.radioB_dirrecionIzquierda)


        self.verticalLayout_16.addLayout(self.verticalLayout_13)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(120, 0, 121, 141))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_14)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.radioB_estiloBarras = QRadioButton(self.frame_10)
        self.radioB_estiloBarras.setObjectName(u"radioB_estiloBarras")
        self.radioB_estiloBarras.setChecked(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.radioB_estiloBarras)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_12)

        self.radioB_estiloCirculos = QRadioButton(self.frame_10)
        self.radioB_estiloCirculos.setObjectName(u"radioB_estiloCirculos")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.radioB_estiloCirculos)

        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_13)

        self.radioB_estiloEspectro = QRadioButton(self.frame_10)
        self.radioB_estiloEspectro.setObjectName(u"radioB_estiloEspectro")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.radioB_estiloEspectro)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_17)

        self.radioB_estiloAngulo = QRadioButton(self.frame_10)
        self.radioB_estiloAngulo.setObjectName(u"radioB_estiloAngulo")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.radioB_estiloAngulo)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_19)


        self.verticalLayout_12.addLayout(self.formLayout_3)


        self.verticalLayout_17.addLayout(self.verticalLayout_12)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 111, 211))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.spinB_nSteps = QSpinBox(self.frame_11)
        self.spinB_nSteps.setObjectName(u"spinB_nSteps")
        self.spinB_nSteps.setAlignment(Qt.AlignCenter)
        self.spinB_nSteps.setMinimum(3)
        self.spinB_nSteps.setMaximum(200)
        self.spinB_nSteps.setValue(18)

        self.verticalLayout_10.addWidget(self.spinB_nSteps)


        self.verticalLayout_15.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.doubleS_solidPercent = QDoubleSpinBox(self.frame_11)
        self.doubleS_solidPercent.setObjectName(u"doubleS_solidPercent")
        self.doubleS_solidPercent.setAlignment(Qt.AlignCenter)
        self.doubleS_solidPercent.setMinimum(0.100000000000000)
        self.doubleS_solidPercent.setMaximum(0.900000000000000)
        self.doubleS_solidPercent.setSingleStep(0.100000000000000)
        self.doubleS_solidPercent.setValue(0.700000000000000)

        self.verticalLayout_11.addWidget(self.doubleS_solidPercent)


        self.verticalLayout_15.addLayout(self.verticalLayout_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.spinB_minDetection = QSpinBox(self.frame_11)
        self.spinB_minDetection.setObjectName(u"spinB_minDetection")
        self.spinB_minDetection.setAlignment(Qt.AlignCenter)
        self.spinB_minDetection.setMaximum(100)
        self.spinB_minDetection.setValue(0)

        self.verticalLayout_14.addWidget(self.spinB_minDetection)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.horizontalLayout_6.addLayout(self.verticalLayout_15)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 380, 345, 71))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_18)

        self.horizontalS_velocidad = QSlider(self.frame_12)
        self.horizontalS_velocidad.setObjectName(u"horizontalS_velocidad")
        self.horizontalS_velocidad.setMinimum(1)
        self.horizontalS_velocidad.setMaximum(25)
        self.horizontalS_velocidad.setValue(10)
        self.horizontalS_velocidad.setSliderPosition(10)
        self.horizontalS_velocidad.setOrientation(Qt.Horizontal)
        self.horizontalS_velocidad.setInvertedAppearance(True)
        self.horizontalS_velocidad.setInvertedControls(False)
        self.horizontalS_velocidad.setTickPosition(QSlider.TicksBothSides)
        self.horizontalS_velocidad.setTickInterval(10)

        self.verticalLayout_18.addWidget(self.horizontalS_velocidad)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(345, 130))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.lcdN_calibrarDB = QLCDNumber(self.frame_6)
        self.lcdN_calibrarDB.setObjectName(u"lcdN_calibrarDB")
        self.lcdN_calibrarDB.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(5)
        self.lcdN_calibrarDB.setFont(font)
        self.lcdN_calibrarDB.setDigitCount(3)
        self.lcdN_calibrarDB.setSegmentStyle(QLCDNumber.Flat)
        self.lcdN_calibrarDB.setProperty("value", 50.000000000000000)

        self.horizontalLayout_4.addWidget(self.lcdN_calibrarDB)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.dial_calibrarDB = QDial(self.frame_6)
        self.dial_calibrarDB.setObjectName(u"dial_calibrarDB")
        self.dial_calibrarDB.setMinimum(1)
        self.dial_calibrarDB.setMaximum(150)
        self.dial_calibrarDB.setValue(50)
        self.dial_calibrarDB.setWrapping(False)
        self.dial_calibrarDB.setNotchTarget(10.000000000000000)
        self.dial_calibrarDB.setNotchesVisible(True)

        self.verticalLayout_5.addWidget(self.dial_calibrarDB)

        self.label_dB_2 = QLabel(self.frame_6)
        self.label_dB_2.setObjectName(u"label_dB_2")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        self.label_dB_2.setFont(font1)
        self.label_dB_2.setAlignment(Qt.AlignCenter)
        self.label_dB_2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_dB_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(80, 60))
        self.frame.setMaximumSize(QSize(80, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 61, 41))
        self.layout_lcd = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_lcd.setObjectName(u"layout_lcd")
        self.layout_lcd.setContentsMargins(9, 9, 9, 9)

        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.lcdN_calibrarRango = QLCDNumber(self.frame_6)
        self.lcdN_calibrarRango.setObjectName(u"lcdN_calibrarRango")
        self.lcdN_calibrarRango.setMaximumSize(QSize(16777215, 20))
        self.lcdN_calibrarRango.setFont(font)
        self.lcdN_calibrarRango.setDigitCount(3)
        self.lcdN_calibrarRango.setSegmentStyle(QLCDNumber.Flat)
        self.lcdN_calibrarRango.setProperty("value", 45.000000000000000)
        self.lcdN_calibrarRango.setProperty("intValue", 45)

        self.horizontalLayout_2.addWidget(self.lcdN_calibrarRango)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.dial_calibrarRango = QDial(self.frame_6)
        self.dial_calibrarRango.setObjectName(u"dial_calibrarRango")
        self.dial_calibrarRango.setMinimum(1)
        self.dial_calibrarRango.setMaximum(120)
        self.dial_calibrarRango.setValue(60)
        self.dial_calibrarRango.setWrapping(False)
        self.dial_calibrarRango.setNotchTarget(10.000000000000000)
        self.dial_calibrarRango.setNotchesVisible(True)

        self.verticalLayout_6.addWidget(self.dial_calibrarRango)

        self.label_dB_3 = QLabel(self.frame_6)
        self.label_dB_3.setObjectName(u"label_dB_3")
        self.label_dB_3.setFont(font1)
        self.label_dB_3.setAlignment(Qt.AlignCenter)
        self.label_dB_3.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_dB_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushB_start = QPushButton(self.frame_6)
        self.pushB_start.setObjectName(u"pushB_start")
        self.pushB_start.setMaximumSize(QSize(60, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        self.pushB_start.setFont(font2)

        self.verticalLayout_4.addWidget(self.pushB_start)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.pushB_stop = QPushButton(self.frame_6)
        self.pushB_stop.setObjectName(u"pushB_stop")
        self.pushB_stop.setMaximumSize(QSize(60, 16777215))
        self.pushB_stop.setFont(font2)

        self.verticalLayout_4.addWidget(self.pushB_stop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.verticalSpacer_4 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DVumetro", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"COLOR FONDO", None))
        self.radioB_backgroundBlack.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Negro", None))
        self.radioB_backgroundGrey.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Gris", None))
        self.radioB_backgroundWhite.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Blanco", None))
#if QT_CONFIG(tooltip)
        self.radioB_backgroundCustom.setToolTip(QCoreApplication.translate("Form", u"Color personalizado en hexadecimal", None))
#endif // QT_CONFIG(tooltip)
        self.radioB_backgroundCustom.setText("")
#if QT_CONFIG(tooltip)
        self.lineE_backgroundCustomColor.setToolTip(QCoreApplication.translate("Form", u"Color personalizado en hexadecimal", None))
#endif // QT_CONFIG(tooltip)
        self.lineE_backgroundCustomColor.setText(QCoreApplication.translate("Form", u"#483D8B", None))
        self.lineE_backgroundCustomColor.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"COLOR ", None))
        self.radioB_barColorAzul.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Azul ", None))
        self.radioB_barColorRosa.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Rosa", None))
        self.radioB_barColorMoradoCascada.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Morado cascada", None))
        self.radioB_barColorArcoirisCascada.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Arcoiris cascada", None))
        self.radioB_barColorCustom.setText("")
        self.plainT_barColorCustom.setPlainText(QCoreApplication.translate("Form", u"#5e4fa2, #3288bd,#66c2a5", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"DIRECCION", None))
        self.radioB_dirrecionArriba.setText(QCoreApplication.translate("Form", u"Arriba", None))
        self.radioB_dirrecionDerecha.setText(QCoreApplication.translate("Form", u"Derecha", None))
        self.radioB_dirrecionAbajo.setText(QCoreApplication.translate("Form", u"Abajo", None))
        self.radioB_dirrecionIzquierda.setText(QCoreApplication.translate("Form", u"Izquierda", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"ESTILO VUMETRO", None))
        self.radioB_estiloBarras.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Barras", None))
        self.radioB_estiloCirculos.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Circulos", None))
        self.radioB_estiloEspectro.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"Espectro", None))
        self.radioB_estiloAngulo.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"Angulo", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"N\u00ba Barras", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"% Pintado", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Min detenci\u00f3n", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"VELOCIDAD DE MUESTREO", None))
        self.label_dB_2.setText(QCoreApplication.translate("Form", u"Calibrar dB", None))
        self.label_dB_3.setText(QCoreApplication.translate("Form", u"Calibrar Rango", None))
        self.pushB_start.setText(QCoreApplication.translate("Form", u"START", None))
        self.pushB_stop.setText(QCoreApplication.translate("Form", u"STOP", None))
    # retranslateUi

