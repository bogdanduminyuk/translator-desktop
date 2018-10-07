from PyQt5.QtWidgets import QDialog, QMessageBox
from gui.base.mainwindow import Ui_MainWindow
from gui.implementation.settings import Ui_DialogSettingsImplementation
from core.db import Database


class MainWindowImplementation(Ui_MainWindow):
    def __init__(self, owner):
        super(MainWindowImplementation, self).__init__()
        self.owner = owner

    def setupUi(self, MainWindow):
        super(MainWindowImplementation, self).setupUi(MainWindow)
        self.actionOpen.triggered.connect(self.open)
        self.actionAbout.triggered.connect(self.about)
        self.actionOpenSettings.triggered.connect(self.settings)
        self.pushButton.clicked.connect(self.find)
        self.groupBoxProgress.setVisible(False)
        count = Database.count()
        self.statusbar.showMessage("В базе {} слов".format(count))

    def open(self):
        self.statusbar.showMessage("open")

    def about(self):
        msg_box = QMessageBox(self.owner)
        msg_box.setWindowTitle("О программе")
        msg_box.setText("Программа-переводчик слов.\nВерсия 1.0")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()

    def settings(self):
        settingsDialog = QDialog(self.owner)
        ui = Ui_DialogSettingsImplementation()
        ui.setupUi(settingsDialog)
        settingsDialog.exec_()

    def find(self):
        words = self.textEdit.toPlainText()
        options = {
            "syn": self.checkBoxSynonyms.isChecked(),
            "ant": self.checkBoxAntonyms.isChecked(),
            "def": self.checkBoxDefinitons.isChecked(),
        }

        self.groupBoxProgress.setVisible(True)
