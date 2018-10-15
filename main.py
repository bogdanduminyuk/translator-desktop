import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication(sys.argv)
window = QMainWindow()

try:
    from gui.implementation.mainwindow import MainWindowImplementation

    ui = MainWindowImplementation(window)
    ui.setupUi(window)
    window.show()
except Exception as e:
    msg_box = QMessageBox(window)
    msg_box.setWindowTitle("Ошибка")
    msg_box.setText(str(e))
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.exec_()
    sys.exit(-1)
else:
    sys.exit(app.exec_())
