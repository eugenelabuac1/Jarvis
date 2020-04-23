#Class for controlling the windows
from PyQt5 import QtCore, QtGui, QtWidgets
from Jarvis_MainWindow import Ui_Jarvis
from Jarvis_HelpWindow import Ui_HelpWindow
from Jarvis_HistoryWindow import Ui_History
class ShowWindow:

    def __init__(self):
        pass

    def Show_FirstWindow(self):

        self.Jarvis = QtWidgets.QMainWindow()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self.Jarvis)
        self.ui.pushHelp.clicked.connect(self.Show_SecondWindow)
        self.Jarvis.show()

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

   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = ShowWindow()
    win.Show_FirstWindow()
    sys.exit(app.exec_())
