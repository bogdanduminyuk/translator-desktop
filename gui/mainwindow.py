# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 341, 241))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 210, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 50, 171, 151))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 121, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxSynonyms = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxSynonyms.setObjectName("checkBoxSynonyms")
        self.verticalLayout.addWidget(self.checkBoxSynonyms)
        self.checkBoxAntonyms = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxAntonyms.setObjectName("checkBoxAntonyms")
        self.verticalLayout.addWidget(self.checkBoxAntonyms)
        self.checkBoxDefinitons = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxDefinitons.setObjectName("checkBoxDefinitons")
        self.verticalLayout.addWidget(self.checkBoxDefinitons)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpenSettings = QtWidgets.QAction(MainWindow)
        self.actionOpenSettings.setObjectName("actionOpenSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionOpenSettings)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator v1.0"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Введите слова для поиска..."))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.groupBox.setTitle(_translate("MainWindow", "Опции"))
        self.checkBoxSynonyms.setText(_translate("MainWindow", "Синонимы"))
        self.checkBoxAntonyms.setText(_translate("MainWindow", "Антонимы"))
        self.checkBoxDefinitons.setText(_translate("MainWindow", "Определения"))
        self.label.setText(_translate("MainWindow", "Слова:"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Инструменты"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Выход"))
        self.actionOpenSettings.setText(_translate("MainWindow", "Настройки..."))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))

