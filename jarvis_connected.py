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
import sqlite3
import datetime
new = 2
tabUrl="http://google.com/?#q="
speak = wincl.Dispatch("SAPI.SpVoice")
conn = sqlite3.connect('test.db')
c = conn.cursor()
#c.execute("""CREATE TABLE history (
 #       action_type text,
  #      content text,
   #     date text)""")
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
                    add_history('search',text[14:])
                    
                                                          
                                        
                if text == "jarvis open notepad":
                    speak.speak("Opening notepad")
                    os.system("start notepad.exe")
                    add_history('open', 'notepad')
                    
                if text == "jarvis open chrome":
                    speak.speak("Opening chrome")
                    os.system("start chrome.exe")
                    add_history('open', 'chrome')
                    
                if text == "jarvis open word":
                    speak.speak("Opening word")
                    os.system("start WINWORD.exe")
                    add_history('open', 'word')
                
                if text == "jarvis shutdown computer":
                    speak.speak("Shutting down pc in 20 seconds.")
                    #os.system("shutdown /s /t 20")
                    print("shutdown")
                    add_history('shutdown', '')
                    
                if text == "jarvis restart computer":
                    speak.Speak("Restarting pc in 20 seconds.")
                    #os.system("shutdown /r /t 20")
                    print("restart")
                    add_history('restart', '')
                    
                if text == "jarvis display history":
                    speak.Speak("Displaying command history.")
                    show_history()
                
                if text == "jarvis clear history":
                    speak.Speak("Deleting command history.")
                    clear_history()
                    show_history()
            except:
                speak.Speak("Sorry I could not recognize what you said")
                
            
            conn.commit()
            conn.close 
        def add_history(action_type,content):
            currentDT = str(datetime.datetime.now()) 
            c.execute("INSERT INTO history VALUES ('{}', '{}', '{}' )".format(action_type,content,currentDT[:16]))
            conn.commit()
            conn.close
            
        def show_history():
            c.execute('SELECT * FROM history')
            print(c.fetchall())
        
        def clear_history():
            c.execute("DELETE from history")
            conn.commit()
            conn.close
        
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setWindowIcon(QtGui.QIcon("logo.jpg"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(190, 340, 111, 61))
        self.button.setObjectName("button")
        self.button.setIcon(QtGui.QIcon(QtGui.QPixmap("mic.jpg")))
        self.button.setIconSize(QtCore.QSize(50,50))
                
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
                
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.button.clicked.connect(Test)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis"))
        
        self.label.setText(_translate("MainWindow", "WELCOME TO JARVIS"))
    
    
    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

