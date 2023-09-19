"""
                                    ******
    Author:     P. Matten & G. Giardina
    Contact:    philipp.matten@meduniwien.ac.at & gabriel.giardina@meduniwien.ac.at
                                    ******
                                         
        >>> main file for Laser Setup GUI creation, methods and handling     
                                
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.animation as animation
from PyQt5 import QtCore, QtGui, QtWidgets

# custom imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src')))
from spectrometerreadout import SpectrometerReadOuts


class UiWindowDialog(object):
    
    def __init__(self) -> None:
        self.Spec = SpectrometerReadOuts()
        
    def setupUi(self, mainWindow_Dialog):
        mainWindow_Dialog.setObjectName("mainWindow_Dialog")
        mainWindow_Dialog.resize(620, 500)
        self.openGLWidget = QtWidgets.QOpenGLWidget(mainWindow_Dialog)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 10, 450, 250))
        self.openGLWidget.setObjectName("openGLWidget")
        self.inputBox_IntegrationTime = QtWidgets.QTextEdit(mainWindow_Dialog)
        self.inputBox_IntegrationTime.setGeometry(QtCore.QRect(10, 290, 80, 25))
        self.inputBox_IntegrationTime.setObjectName("inputBox_IntegrationTime")
        self.label_IntegrationTime = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_IntegrationTime.setGeometry(QtCore.QRect(10, 260, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_IntegrationTime.setFont(font)
        self.label_IntegrationTime.setObjectName("label_IntegrationTime")
        self.textBrowser_Averaging = QtWidgets.QTextBrowser(mainWindow_Dialog)
        self.textBrowser_Averaging.setGeometry(QtCore.QRect(120, 290, 80, 25))
        self.textBrowser_Averaging.setObjectName("textBrowser_Averaging")
        self.label_Averaging = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_Averaging.setGeometry(QtCore.QRect(130, 260, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_Averaging.setFont(font)
        self.label_Averaging.setObjectName("label_Averaging")
        self.pushButton_SaveSpectum = QtWidgets.QPushButton(mainWindow_Dialog)
        self.pushButton_SaveSpectum.setGeometry(QtCore.QRect(230, 290, 80, 25))
        self.pushButton_SaveSpectum.setObjectName("pushButton_SaveSpectum")
        self.label_SaveSpectrum = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_SaveSpectrum.setGeometry(QtCore.QRect(230, 260, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_SaveSpectrum.setFont(font)
        self.label_SaveSpectrum.setObjectName("label_SaveSpectrum")
        self.label_RecallSpectrum = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_RecallSpectrum.setGeometry(QtCore.QRect(350, 260, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_RecallSpectrum.setFont(font)
        self.label_RecallSpectrum.setObjectName("label_RecallSpectrum")
        self.pushButton_RecallSpectrum = QtWidgets.QPushButton(mainWindow_Dialog)
        self.pushButton_RecallSpectrum.setGeometry(QtCore.QRect(350, 290, 100, 25))
        self.pushButton_RecallSpectrum.setObjectName("pushButton_RecallSpectrum")
        self.checkBox = QtWidgets.QCheckBox(mainWindow_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(480, 10, 125, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.slider_LaserPower = QtWidgets.QSlider(mainWindow_Dialog)
        self.slider_LaserPower.setGeometry(QtCore.QRect(480, 70, 111, 20))
        self.slider_LaserPower.setOrientation(QtCore.Qt.Horizontal)
        self.slider_LaserPower.setObjectName("slider_LaserPower")
        self.label_LaserPowerSlider = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_LaserPowerSlider.setGeometry(QtCore.QRect(480, 45, 110, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_LaserPowerSlider.setFont(font)
        self.label_LaserPowerSlider.setObjectName("label_LaserPowerSlider")
        self.display_LaserAmplitude = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_LaserAmplitude.setGeometry(QtCore.QRect(530, 110, 65, 25))
        self.display_LaserAmplitude.setObjectName("display_LaserAmplitude")
        self.label_Amplitude = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_Amplitude.setGeometry(QtCore.QRect(480, 110, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_Amplitude.setFont(font)
        self.label_Amplitude.setObjectName("label_Amplitude")
        self.label_Power = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_Power.setGeometry(QtCore.QRect(480, 140, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_Power.setFont(font)
        self.label_Power.setObjectName("label_Power")
        self.display_LaserPower = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_LaserPower.setGeometry(QtCore.QRect(530, 140, 65, 25))
        self.display_LaserPower.setObjectName("display_LaserPower")
        self.display_TDB1 = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_TDB1.setGeometry(QtCore.QRect(530, 170, 65, 25))
        self.display_TDB1.setObjectName("display_TDB1")
        self.display_TBD2 = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_TBD2.setGeometry(QtCore.QRect(530, 200, 65, 25))
        self.display_TBD2.setObjectName("display_TBD2")
        self.label_TBD1 = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_TBD1.setGeometry(QtCore.QRect(480, 170, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_TBD1.setFont(font)
        self.label_TBD1.setObjectName("label_TBD1")
        self.label_TBD2 = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_TBD2.setGeometry(QtCore.QRect(480, 200, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_TBD2.setFont(font)
        self.label_TBD2.setObjectName("label_TBD2")
        self.display_SlitApertureDisplay = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_SlitApertureDisplay.setGeometry(QtCore.QRect(15, 370, 60, 25))
        self.display_SlitApertureDisplay.setObjectName("display_SlitApertureDisplay")
        self.label_SlitAperture = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_SlitAperture.setGeometry(QtCore.QRect(15, 340, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_SlitAperture.setFont(font)
        self.label_SlitAperture.setObjectName("label_SlitAperture")
        self.textEdit_SlitApertureStepperMotorInput = QtWidgets.QTextEdit(mainWindow_Dialog)
        self.textEdit_SlitApertureStepperMotorInput.setGeometry(QtCore.QRect(120, 370, 70, 25))
        self.textEdit_SlitApertureStepperMotorInput.setObjectName("textEdit_SlitApertureStepperMotorInput")
        self.label_SlitApertureStepperMotorInputBox = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_SlitApertureStepperMotorInputBox.setGeometry(QtCore.QRect(120, 340, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_SlitApertureStepperMotorInputBox.setFont(font)
        self.label_SlitApertureStepperMotorInputBox.setObjectName("label_SlitApertureStepperMotorInputBox")
        self.display_SlitPosition = QtWidgets.QLCDNumber(mainWindow_Dialog)
        self.display_SlitPosition.setGeometry(QtCore.QRect(15, 430, 60, 25))
        self.display_SlitPosition.setObjectName("display_SlitPosition")
        self.label_SlitPosition = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_SlitPosition.setGeometry(QtCore.QRect(15, 400, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_SlitPosition.setFont(font)
        self.label_SlitPosition.setObjectName("label_SlitPosition")
        self.textBrowser_SlitPositionInput = QtWidgets.QTextBrowser(mainWindow_Dialog)
        self.textBrowser_SlitPositionInput.setGeometry(QtCore.QRect(120, 430, 70, 25))
        self.textBrowser_SlitPositionInput.setObjectName("textBrowser_SlitPositionInput")
        self.label_SlitPositionInputBox = QtWidgets.QLabel(mainWindow_Dialog)
        self.label_SlitPositionInputBox.setGeometry(QtCore.QRect(120, 400, 100, 25))
        
        # Slit position input box
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_SlitPositionInputBox.setFont(font)
        self.label_SlitPositionInputBox.setObjectName("label_SlitPositionInputBox")
        
        # Close button
        self.pushButton_CloseApp = QtWidgets.QPushButton(mainWindow_Dialog)
        self.pushButton_CloseApp.setGeometry(QtCore.QRect(510, 440, 95, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CloseApp.setFont(font)
        self.pushButton_CloseApp.setObjectName("pushButton_CloseApp")
        self.close_application_via_button()  

        self.retranslateUi(mainWindow_Dialog)
        QtCore.QMetaObject.connectSlotsByName(mainWindow_Dialog)

    def retranslateUi(self, mainWindow_Dialog):
        _translate = QtCore.QCoreApplication.translate
        mainWindow_Dialog.setWindowTitle(_translate("mainWindow_Dialog", "Dialog"))
        self.label_IntegrationTime.setText(_translate("mainWindow_Dialog", "Integration Time"))
        self.label_Averaging.setText(_translate("mainWindow_Dialog", "Averaging"))
        self.pushButton_SaveSpectum.setText(_translate("mainWindow_Dialog", "Save"))
        self.label_SaveSpectrum.setText(_translate("mainWindow_Dialog", "Save Spectrum"))
        self.label_RecallSpectrum.setText(_translate("mainWindow_Dialog", "Recall Spectrum"))
        self.pushButton_RecallSpectrum.setText(_translate("mainWindow_Dialog", "Recall"))
        self.checkBox.setText(_translate("mainWindow_Dialog", "Laser enabled"))
        self.label_LaserPowerSlider.setText(_translate("mainWindow_Dialog", "Laser Power"))
        self.label_Amplitude.setText(_translate("mainWindow_Dialog", "Amp."))
        self.label_Power.setText(_translate("mainWindow_Dialog", "Pow."))
        self.label_TBD1.setText(_translate("mainWindow_Dialog", "TBD1"))
        self.label_TBD2.setText(_translate("mainWindow_Dialog", "TBD2"))
        self.label_SlitAperture.setText(_translate("mainWindow_Dialog", "Slit Aperture"))
        self.label_SlitApertureStepperMotorInputBox.setText(_translate("mainWindow_Dialog", "Slit Aperture"))
        self.label_SlitPosition.setText(_translate("mainWindow_Dialog", "Slit Position"))
        self.label_SlitPositionInputBox.setText(_translate("mainWindow_Dialog", "Slit Position "))
        self.pushButton_CloseApp.setText(_translate("mainWindow_Dialog", "Close"))

    ### --- custom functions and signals --- ###
    
    ## TODO: Continue here
    # spectrometer curve display
    def display_spectrometer_data(self):        
        fig = Figure(figsize=(3, 1.8), dpi=300)
        canvas = FigureCanvasAgg(fig)
        ax = fig.add_subplot(111)
        def animate(i):
            wavelengths, intensities = self.Spec().read_out_spectrometer_data()
            ax.clear()
            ax.plot(wavelengths, intensities)
        # TODO: get integration time from signal
        intTime = 100
        spec_plot = animation.FuncAnimation(fig , animate , interval = intTime/1000) # interval in µs. ms/µs conversion is important!
        canvas.draw()
        buffer = canvas.buffer_rgba() # already a RGBA buffer - no conversion nec.
        buffer = np.asarray(buffer)
        disp_img = QtGui.QImage(buffer.data.tobytes(), 
                                buffer.shape[1], buffer.shape[0], 
                                QtGui.QImage.Format_ARGB32)
        # TODO: check OpenGL widget docs for conversion of plots
        # self.openGLWidget.setPixmap( QtGui.QPixmap(disp_img) )
        # self.openGLWidget.setScaledContents(True) 
        
        
    # close application from button
    def close_application_via_button(self) :
        """ closes GUI via the CLOSE button -> terminates application """
        self.pushButton_CloseApp.clicked.connect(QtCore.QCoreApplication.instance().quit)


def run_application() :
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiWindowDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
        
        
if __name__ == "__main__":
    run_application()
