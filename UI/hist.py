# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append('../')
from BLL.application import *
from PyQt5 import QtCore, QtGui, QtWidgets
from DAL.db import *

class ShowWindow3:

    def __init__(self):
        pass
        
    def Show_ThirdWindow(self,action):
        self.History = QtWidgets.QMainWindow()
        self.ui = Ui_History()
        self.action = action
        self.ui.setupUi(self.History, self.action)
        self.History.show()    
        
        
class Ui_History(object):
    def setupUi(self, Ui_History, action):
        Ui_History.setObjectName("Ui_History")
        Ui_History.resize(380, 380)
        self.centralwidget = QtWidgets.QWidget(Ui_History)
        self.centralwidget.setObjectName("centralwidget")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_History.setWindowIcon(icon)
        
        #scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 0, 430, 430))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #setting up dbTable

        self.dbTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dbTable.setGeometry(QtCore.QRect(10, 10, 370, 350))
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
        conn = sqlite3.connect('DAL\JarvisDatabase.db') 
        result = conn.execute(action)
        for row_number, row_data in enumerate(result):
            self.dbTable.insertRow(row_number)  
            for column_number, data in enumerate(row_data):
                self.dbTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()
        