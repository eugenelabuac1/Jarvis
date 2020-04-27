''' UI of Jarvis '''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
          

        Jarvis.setObjectName("Jarvis")
        Jarvis.setFixedSize(597, 600)
        
    
        
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
        self.labelJarvis.setProperty("icon", QtGui.QPixmap("JARVIS.png"))
        self.labelJarvis.setObjectName("labelJarvis")
        
        #Input for Text to Speech
        self.txtsp = QtWidgets.QLineEdit(self.centralwidget)
        self.txtsp.setGeometry(QtCore.QRect(0, 530, 341, 71))
        self.txtsp.setText("")
        self.txtsp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txtsp.setObjectName("lineEdit")
        
        #Button for pushing Text
        self.pushText = QtWidgets.QPushButton(self.centralwidget)
        self.pushText.setEnabled(True)
        self.pushText.setGeometry(QtCore.QRect(360, 530, 71, 71))
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
        self.label_gif.setMovie(wave)
        wave.start()
        #Manual Mic
        self.pushMic = QtWidgets.QPushButton(self.centralwidget)
        self.pushMic.setGeometry(QtCore.QRect(520, 530, 71, 71))
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
        self.pushMic_2.setGeometry(QtCore.QRect(440, 530, 71, 71))
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
        self.label_2.setGeometry(QtCore.QRect(540, 520, 47, 13))
        self.label_2.setObjectName("label_2")
        
        #Automatic Label
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(450, 520, 47, 13))
        self.label_A.setObjectName("label_A")
        Jarvis.setCentralWidget(self.centralwidget)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(390, 370, 201, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labelStatus= QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelStatus.setGeometry(QtCore.QRect(0, 0, 201, 121))
        self.labelStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.labelStatus.setScaledContents(True)
        self.labelStatus.setObjectName("labelStatus")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        
        def Status():
            inp = self.txtsp.text()
            self.labelStatus.setText("\nYou typed: \n \n" + inp)
            self.txtsp.setText("") 

        
        self.pushText.clicked.connect(Status)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)
    
        

    
       

    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "Jarvis"))
        self.txtsp.setPlaceholderText(_translate("MainWindow", "Please Input Text"))
        
        self.label_2.setText(_translate("Jarvis", "Manual"))
        self.label_A.setText(_translate("Jarvis", "Automatic"))



        
        
        
#Another class for the ui of the help window       
class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.setFixedSize(632, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpWindow.setWindowIcon(icon)
        HelpWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Scroll Bar
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 0, 641, 601))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 622, 1417))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Instructions of jarvis
        self.help = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.help.setText("")
        self.help.setPixmap(QtGui.QPixmap("jarvis help.jpg"))
        self.help.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.help.setObjectName("label")
        self.verticalLayout.addWidget(self.help)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Jarvis-Help"))
        
        

        

class ShowWindow:

    def __init__(self):
        pass

    def Show_FirstWindow(self):

        self.Jarvis = QtWidgets.QMainWindow()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self.Jarvis)
        self.ui.pushHelp.clicked.connect(self.Show_SecondWindow)
        self.Jarvis.show()

        #Functionality of the button
        self.ui.pushMic.clicked.connect(commands)
         
    def Show_SecondWindow(self):
        
        self.HelpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.HelpWindow)       
        self.HelpWindow.show()
        
    def Show_ThirdWindow(self,action):
        self.History = QtWidgets.QMainWindow()
        self.ui = Ui_History()
        self.ui.setupUi(self.History, action)
        self.History.show()    
    
class Ui_History(object):
    def setupUi(self, Ui_History,action):
        Ui_History.setObjectName("Ui_History")
        Ui_History.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_History.setWindowIcon(icon)        
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
    sys.path.append('../')
    from Application.application import *
    app = QtWidgets.QApplication(sys.argv)
    win = ShowWindow()
    win.Show_FirstWindow()
    sys.exit(app.exec_())