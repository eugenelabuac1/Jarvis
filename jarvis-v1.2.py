# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import win32com.client as wincl
import sqlite3 
import speech_recognition as sr
import os
import webbrowser
new = 2
tabUrl="http://google.com/?#q="
speak = wincl.Dispatch("SAPI.SpVoice")


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def Test():
            r = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("say something")
                    audio = r.listen(source,timeout=3, phrase_time_limit=3)
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                
                if text[0:13] == "jarvis search":
                    speak.speak("Searching {}".format(text[14:]))
                    webbrowser.open(tabUrl+text[14:], new=new)
                    
                if text == "jarvis open notepad":
                    speak.speak("Opening notepad")
                    os.system("start notepad.exe")
                    
                if text == "jarvis open chrome":
                    speak.speak("Opening chrome")
                    os.system("start chrome.exe")
                    
                if text == "jarvis open word":
                    speak.speak("Opening word")
                    os.system("start WINWORD.exe")
                
                if text == "jarvis shutdown computer":
                    speak.speak("Shutting down pc in 20 seconds.")
                    #os.system("shutdown /s /t 20")
                    print("shutdown")
                    
                if text == "jarvis restart computer":
                    speak.Speak("Restarting pc in 20 seconds.")
                    #os.system("shutdown /r /t 20")
                    print("restart")
            
            except:
                speak.Speak("Sorry I could not recognize what you said")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushMic = QtWidgets.QPushButton(self.centralwidget)
        self.pushMic.setGeometry(QtCore.QRect(420, 330, 81, 71))
        self.pushMic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("mic2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushMic.setIcon(icon1)
        self.pushMic.setIconSize(QtCore.QSize(50, 50))
        self.pushMic.setShortcut("")
        self.pushMic.setDefault(False)
        self.pushMic.setFlat(False)
        self.pushMic.setObjectName("pushMic")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 501, 131))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("JARVIS.png"))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setProperty("icon", QtGui.QPixmap("JARVIS.png"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 260, 271, 71))
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.pushText = QtWidgets.QPushButton(self.centralwidget)
        self.pushText.setEnabled(True)
        self.pushText.setGeometry(QtCore.QRect(100, 330, 81, 71))
        self.pushText.setAccessibleDescription("")
        self.pushText.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("wicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushText.setIcon(icon2)
        self.pushText.setIconSize(QtCore.QSize(50, 50))
        self.pushText.setProperty("pixmap", QtGui.QPixmap("wicon.png"))
        self.pushText.setObjectName("pushText")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 0, 75, 51))
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushMic.clicked.connect(Test)

    



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Please input text to convert to speech"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

