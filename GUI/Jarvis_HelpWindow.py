#Another class for the ui of the help window       
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(495, 543)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpWindow.setWindowIcon(icon)
        HelpWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Jarvis-Help"))
        self.label.setText(_translate("HelpWindow", "How to use Jarvis"))