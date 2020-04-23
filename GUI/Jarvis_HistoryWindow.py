
#Class for History GUI
import win32com.client as wincl 
import sqlite3
new = 2
tabUrl="http://google.com/?#q="
speak = wincl.Dispatch("SAPI.SpVoice")
conn = sqlite3.connect('test1.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history (action_type text, content text, date text)""")
from PyQt5 import QtCore, QtGui, QtWidgets

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

