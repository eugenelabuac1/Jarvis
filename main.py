if __name__ == "__main__":
    from UI.ui import *
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = ShowWindow()
    win.Show_FirstWindow()
    sys.exit(app.exec_())