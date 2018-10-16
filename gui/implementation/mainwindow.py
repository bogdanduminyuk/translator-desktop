from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from core import translator
from gui.base.mainwindow import Ui_MainWindow


class MainWindowImplementation(Ui_MainWindow):
    def __init__(self, owner):
        self.owner = owner
        self.child_thread = None

    def setupUi(self, MainWindow):
        super(MainWindowImplementation, self).setupUi(MainWindow)
        self.pushButtonFind.clicked.connect(self.find)
        self.actionReset.triggered.connect(self.reset)
        self.progressBar.hide()

    def reset(self):
        self.checkBoxDefinitions.setChecked(False)
        self.checkBoxAntonyms.setChecked(False)
        self.checkBoxSynonyms.setChecked(False)
        self.checkBoxTranslate.setChecked(False)
        self.plainTextEditLog.setEnabled(False)
        self.plainTextEditLog.clear()
        self.plainTextInputWords.clear()
        self.progressBar.hide()

        for idx in range(1, 5):
            self.tableWidgetResult.setColumnHidden(idx, False)

        self.pushButtonFind.setEnabled(True)

    def find(self):
        skip_columns = 1
        options = [
            self.checkBoxTranslate.isChecked(),
            self.checkBoxSynonyms.isChecked(),
            self.checkBoxAntonyms.isChecked(),
            self.checkBoxDefinitions.isChecked(),
        ]
        # TODO: add class validator
        # check if True in checkboxes
        if True not in options:
            QMessageBox.information(self.owner, "Внимание", "Пожалуйста, отметье галочками то, что хотите найти!")
            return

        # hide columns with False in options
        for idx, option in enumerate(options, skip_columns):
            self.tableWidgetResult.setColumnHidden(idx, not option)

        # turn off actionReset and push button to prevent clicking and triggering during processing
        self.pushButtonFind.setEnabled(False)
        self.actionReset.setEnabled(False)

        self.plainTextEditLog.setEnabled(True)
        self.progressBar.setVisible(True)

        word_list = ["word" + str(i) for i in range(10)]
        self.progressBar.setMaximum(len(word_list))
        self.progressBar.setValue(0)

        self.child_thread = TranslatorThread(word_list)
        self.child_thread.countChanged.connect(self.update)
        self.child_thread.finish.connect(self.show_results)
        self.child_thread.start()

    def update(self, current, word):
        self.progressBar.setValue(current)
        self.plainTextEditLog.insertPlainText("Ищется слово: " + word)

    def show_results(self):
        QMessageBox.information(self.owner, "Готово!", "Поиск слов успешно завершен.")
        self.pushButtonFind.setEnabled(True)
        self.progressBar.setVisible(False)
        self.actionReset.setEnabled(True)


class TranslatorThread(QThread):
    countChanged = pyqtSignal(int, str)
    finish = pyqtSignal()

    def __init__(self, word_list):
        super(TranslatorThread, self).__init__()
        self.word_list = word_list

    def run(self):
        for i, word in enumerate(self.word_list, 1):
            translator.get(word)
            self.countChanged.emit(i, word)

        self.finish.emit()
