from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from gui.base.mainwindow import Ui_MainWindow
from gui.implementation.settings import Ui_DialogSettingsImplementation

from core.db import Database
from core.input_data_readers import PlainTextReader
from core.result_data_writers import DocDataWriter
from core.functions import get_translation, get_word_from_api


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
            "syn": True,  # self.checkBoxSynonyms.isChecked(),
            "ant": True,  # self.checkBoxAntonyms.isChecked(),
            "def": True,  # self.checkBoxDefinitons.isChecked(),
        }

        reader = PlainTextReader()
        words = reader.read(words)
        total, current = len(words), 0
        output = {}

        self.labelCurrentWord.setText("")
        self.progressBar.setMaximum(total)
        self.groupBoxProgress.setVisible(True)

        for word in words:
            self.labelCurrentWord.setText(word)
            from_db = Database.get(word)

            if from_db:
                output[word] = from_db
            else:
                output[word] = {
                    "api": get_word_from_api(word)[0],
                    "translation": get_translation(word),
                }

                Database.set(word, output[word]["translation"], output[word]["api"])

            current += 1
            self.progressBar.setValue(current)

        path, filter = QFileDialog.getSaveFileName(self.owner, "Сохранить как..", filter="Документ Word (*.docx)")

        try:
            writer = DocDataWriter(path, options)
            writer.write(output)
        except Exception as e:
            self.statusbar.showMessage("Ошибка сохранения файла " + path)
            msg = QMessageBox()
            msg.setWindowTitle("Exception")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.exec_()
        else:
            self.statusbar.showMessage(path + " сохранен успешно")
        finally:
            self.groupBoxProgress.setVisible(False)
