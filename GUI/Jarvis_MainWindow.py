#Jarvis MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        Jarvis.resize(597, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Jarvis.setWindowIcon(icon)
        Jarvis.setAutoFillBackground(False)
        Jarvis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setObjectName("centralwidget")
        self.labelJarvis = QtWidgets.QLabel(self.centralwidget)
        self.labelJarvis.setGeometry(QtCore.QRect(0, 60, 591, 111))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #Welcome to Jarvis
        self.labelJarvis.setFont(font)
        self.labelJarvis.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelJarvis.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelJarvis.setText("")
        self.labelJarvis.setPixmap(QtGui.QPixmap("JARVIS.png"))
        self.labelJarvis.setScaledContents(True)
        self.labelJarvis.setOpenExternalLinks(False)
        self.labelJarvis.setProperty("icon", QtGui.QPixmap("JARVIS.jpf"))
        self.labelJarvis.setObjectName("labelJarvis")

        #Input for Text to Speech
        self.txttspeech = QtWidgets.QTextEdit(self.centralwidget)
        self.txttspeech.setGeometry(QtCore.QRect(0, 430, 351, 71))
        self.txttspeech.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txttspeech.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txttspeech.setDocumentTitle("")
        self.txttspeech.setObjectName("txttspeech")

        #Button for pushing Text
        self.pushText = QtWidgets.QPushButton(self.centralwidget)
        self.pushText.setEnabled(True)
        self.pushText.setGeometry(QtCore.QRect(360, 430, 71, 71))
        self.pushText.setAccessibleDescription("")
        self.pushText.setAutoFillBackground(False)
        self.pushText.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"   \n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.3, fx: 0.3, fy: -0.3,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.4, fx: 0.4, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushText.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("wicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushText.setIcon(icon1)
        self.pushText.setIconSize(QtCore.QSize(60, 60))
        self.pushText.setFlat(True)
        self.pushText.setProperty("pixmap", QtGui.QPixmap("wicon.png"))
        self.pushText.setObjectName("pushText")

        #Help Button
        self.pushHelp = QtWidgets.QPushButton(self.centralwidget)
        self.pushHelp.setGeometry(QtCore.QRect(540, 0, 51, 51))
        self.pushHelp.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"   \n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.3, fx: 0.3, fy: -0.3,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.4, fx: 0.4, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushHelp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("helpp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushHelp.setIcon(icon2)
        self.pushHelp.setIconSize(QtCore.QSize(40, 40))
        self.pushHelp.setFlat(True)
        self.pushHelp.setObjectName("pushHelp")

        #Wave gif
        wave = QtGui.QMovie("wave1.gif")

        self.label_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_gif.setEnabled(True)
        self.label_gif.setGeometry(QtCore.QRect(0, 210, 591, 101))
        self.label_gif.setText("")
        self.label_gif.setScaledContents(True)
        self.label_gif.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_gif.setObjectName("label_gif")


        #Manual Mic
        self.pushMic = QtWidgets.QPushButton(self.centralwidget)
        self.pushMic.setGeometry(QtCore.QRect(520, 430, 71, 71))
        self.pushMic.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"   \n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.3, fx: 0.3, fy: -0.3,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.4, fx: 0.4, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMic.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("mic2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushMic.setIcon(icon3)
        self.pushMic.setIconSize(QtCore.QSize(60, 60))
        self.pushMic.setObjectName("pushMic")

        #Automatic Mic
        self.pushMic_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushMic_2.setGeometry(QtCore.QRect(440, 430, 71, 71))
        self.pushMic_2.setAutoFillBackground(False)
        self.pushMic_2.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"   \n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.3, fx: 0.3, fy: -0.3,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.4, fx: 0.4, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMic_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushMic_2.setIcon(icon4)
        self.pushMic_2.setIconSize(QtCore.QSize(50, 50))
        self.pushMic_2.setCheckable(True)
        self.pushMic_2.setChecked(False)
        self.pushMic_2.setAutoRepeat(False)
        self.pushMic_2.setAutoExclusive(False)
        self.pushMic_2.setAutoRepeatDelay(300)
        self.pushMic_2.setAutoRepeatInterval(100)
        self.pushMic_2.setDefault(False)
        self.pushMic_2.setFlat(False)
        self.pushMic_2.setObjectName("pushMic_2")

        #Manual Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 420, 47, 13))
        self.label_2.setObjectName("label_2")

        #Automatic Label
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(450, 420, 47, 13))
        self.label_A.setObjectName("label_A")
        Jarvis.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)








    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "Jarvis"))
        self.txttspeech.setPlaceholderText(_translate("Jarvis", "Please input text to convert to speech"))
        self.label_2.setText(_translate("Jarvis", "Manual"))
        self.label_A.setText(_translate("Jarvis", "Automatic"))












        

