import sys

from PySide6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
