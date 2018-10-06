from gui.base.mainwindow import Ui_MainWindow


class MainWindowImplementation(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MainWindowImplementation, self).setupUi(MainWindow)
        self.actionOpen.triggered.connect(self.open)
        self.actionAbout.triggered.connect(self.about)
        self.actionOpenSettings.triggered.connect(self.settings)
        self.pushButton.clicked.connect(self.find)

    def open(self):
        self.statusbar.showMessage("open")

    def about(self):
        self.statusbar.showMessage("about")

    def settings(self):
        self.statusbar.showMessage("settings")

    def find(self):
        self.statusbar.showMessage("Find")
