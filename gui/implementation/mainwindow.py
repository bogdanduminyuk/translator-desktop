from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

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

    def update(self, current_idx, word, error):
        self.progressBar.setValue(current_idx)

        if error:
            self.plainTextEditLog.appendHtml("{}... <font color = \"red\">Ошибка! {}</font>".format(word, error))
            self.plainTextEditLog.insertPlainText("\n")
        else:
            self.plainTextEditLog.insertPlainText(word + "... OK!")

    def show_results(self, words):
        QMessageBox.information(self.owner, "Готово!", "Поиск слов успешно завершен.")
        self.pushButtonFind.setEnabled(True)
        self.progressBar.setVisible(False)
        self.actionReset.setEnabled(True)

        col_count = 0
        result_cols_keys = []
        cols_order = "word", "translate", "syn", "ant", "def"

        # keyword: option_enabled, header
        options = {
            "word": (True, "Слово"),
            "translate": (self.checkBoxTranslate.isChecked(), "Перевод"),
            "syn": (self.checkBoxSynonyms.isChecked(), "Синонимы"),
            "ant": (self.checkBoxAntonyms.isChecked(), "Антонимы"),
            "def": (self.checkBoxDefinitions.isChecked(), "Определения")
        }

        self.tableWidgetResult.clear()
        self.tableWidgetResult.setRowCount(len(words))
        self.tableWidgetResult.setColumnCount(len(cols_order))

        # setup headers and table
        for col_key in cols_order:
            enabled, header = options[col_key]
            if enabled:
                self.tableWidgetResult.setHorizontalHeaderItem(col_count, QTableWidgetItem(header))
                result_cols_keys.append(col_key)
                col_count += 1

        self.tableWidgetResult.setColumnCount(len(result_cols_keys))

        # fill table
        for row_idx, word in enumerate(words):
            for col_idx, col_key in enumerate(result_cols_keys):
                self.tableWidgetResult.setItem(row_idx, col_idx, QTableWidgetItem(word.get(col_key, "")))


class TranslatorThread(QThread):
    countChanged = pyqtSignal(int, str, str)
    finish = pyqtSignal(list)

    def __init__(self, word_list):
        super(TranslatorThread, self).__init__()
        self.word_list = word_list

    def run(self):
        words = []
        for i, word in enumerate(self.word_list, 1):
            try:
                word_data = translator.get(word)
                self.countChanged.emit(i, word, "")
            except Exception as e:
                word_data = {"word": word}
                self.countChanged.emit(i, word, str(e))

            words.append(word_data)

        self.finish.emit(words)
