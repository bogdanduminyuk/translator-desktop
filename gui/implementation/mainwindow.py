from gui.base.mainwindow import Ui_MainWindow


class MainWindowImplementation(Ui_MainWindow):
    def __init__(self, owner):
        self.owner = owner
