if __name__ == "__main__":
    from GUI.ui import *
    app = QtWidgets.QApplication(sys.argv)
    win = ShowWindow()
    win.Show_FirstWindow()
    sys.exit(app.exec_())