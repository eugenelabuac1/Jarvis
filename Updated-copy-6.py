

from PyQt5 import QtCore, QtGui, QtWidgets
import win32com.client as wincl 
import speech_recognition as sr
import os
import webbrowser
import sqlite3
import datetime

new = 2
tabUrl="http://google.com/?#q="
speak = wincl.Dispatch("SAPI.SpVoice")
conn = sqlite3.connect('test1.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history (action_type text, content text, date text)""")
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
        self.labelJarvis.setPixmap(QtGui.QPixmap("JARVIS.jpg"))
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
        icon2.addPixmap(QtGui.QPixmap("help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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



        
        
        
#Another class for the ui of the help window       
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
        
        

        

class ShowWindow:

    def __init__(self):
        pass

    def Show_FirstWindow(self):

        self.Jarvis = QtWidgets.QMainWindow()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self.Jarvis)
        self.ui.pushHelp.clicked.connect(self.Show_SecondWindow)
        
        def Test():
            r = sr.Recognizer()
           
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("say something")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
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
                    action = "SELECT * FROM history"
                    Show_ThirdWindow(self,action)
                    show_history()
                
                if text == "jarvis clear history":
                    speak.Speak("Deleting command history.")
                    clear_history()
                    show_history()
                ##
                if text == "jarvis display open":
                    speak.Speak("Displaying history wherein action type is open.")
                    Show_ThirdWindow(self)
                    read_from_db_open()
                    
                if text == "jarvis display search":
                    speak.Speak("Displaying history wherein action type is search.")
                    
                    Show_ThirdWindow(self,action)
                    read_from_db_search()
                    
                if text == "jarvis display restart":
                    speak.Speak("Displaying history wherein action type is restart.")
                    Show_ThirdWindow(self)
                    read_from_db_restart()
                
                if text == "jarvis display shutdown":
                    speak.Speak("Displaying history wherein action type is shutdown.")
                    self.Show_ThirdWindow.show()
                    read_from_db_shutdown()
                ##
            except Exception as e:
                print(e)
                speak.Speak("Sorry I could not recognize what you said")

        #Functionality of the button
        self.ui.pushMic.clicked.connect(Test)
        def Show_ThirdWindow(self,action):
            self.History = QtWidgets.QMainWindow()
            self.ui = Ui_History()
            self.ui.setupUi(self.History, action)
            self.History.show()         
            
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
######
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Table01(datestamp REAL, command TEXT, action TEXT)")
            c.execute("CREATE TABLE IF NOT EXISTS backupTable01(datestamp REAL, command TEXT, action TEXT)")
        
        def read_from_db_open():
            c.execute("SELECT * FROM history WHERE action_type = 'open' ")
            data = c.fetchall()
            print(data)
            for row in data:
                print(row)

        def read_from_db_search():
            c.execute("SELECT * FROM history WHERE action_type = 'search' ")
            data = c.fetchall()
            print(data)
            for row in data:
                print(row)
       
        def read_from_db_restart():
            c.execute("SELECT * FROM history WHERE action_type = 'restart' ")
            data = c.fetchall()
            print(data)
            for row in data:
                print(row) 
            
        def read_from_db_shutdown():
            c.execute("SELECT * FROM history WHERE action_type = 'shutdown' ")
            data = c.fetchall()
            print(data)
            for row in data:
                print(row)                 
            
            conn.commit()
            conn.close 
        self.Jarvis.show()

    def Show_SecondWindow(self):
        
        self.HelpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.HelpWindow)       
        self.HelpWindow.show()
    
class Ui_History(object):
        def setupUi(self, Ui_History,action):
            Ui_History.setObjectName("Ui_History")
            Ui_History.resize(800, 600)
            self.centralwidget = QtWidgets.QWidget(Ui_History)
            self.centralwidget.setObjectName("centralwidget")
            self.dbTable = QtWidgets.QTableWidget(self.centralwidget)
            self.dbTable.setGeometry(QtCore.QRect(10, 10, 781, 571))
            self.dbTable.setGridStyle(QtCore.Qt.SolidLine)
            self.dbTable.setColumnCount(3)
            self.dbTable.setObjectName("dbTable")
            header = self.dbTable.horizontalHeader()
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            self.dbTable.setHorizontalHeaderLabels(("Command;Content;Date and Time").split(";"))
            self.dbTable.horizontalHeader().setMinimumSectionSize(39)
            Ui_History.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(Ui_History)
            self.statusbar.setObjectName("statusbar")
            Ui_History.setStatusBar(self.statusbar)
            self.loadData(action)
            self.retranslateUi(Ui_History)
            QtCore.QMetaObject.connectSlotsByName(Ui_History)

        def retranslateUi(self, Ui_History):
            _translate = QtCore.QCoreApplication.translate
            Ui_History.setWindowTitle(_translate("Ui_History", "History"))
        
        def loadData(self,action):
            conn = sqlite3.connect('test1.db') 
            query = action
            result = conn.execute(query)
            for row_number, row_data in enumerate(result):
                self.dbTable.insertRow(row_number)  
                for column_number, data in enumerate(row_data):
                    self.dbTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            conn.close()   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = ShowWindow()
    win.Show_FirstWindow()
    sys.exit(app.exec_())

