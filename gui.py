import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.implementation.mainwindow import MainWindowImplementation

app = QApplication(sys.argv)
window = QMainWindow()
ui = MainWindowImplementation()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
