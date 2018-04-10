# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameUi.ui'
#
# Created: Tue Apr 10 16:41:21 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fourPlayerStart = QtGui.QPushButton(self.centralwidget)
        self.fourPlayerStart.setGeometry(QtCore.QRect(10, 10, 241, 71))
        self.fourPlayerStart.setObjectName("fourPlayerStart")
        self.mainMenu = QtGui.QPushButton(self.centralwidget)
        self.mainMenu.setGeometry(QtCore.QRect(670, 10, 121, 31))
        self.mainMenu.setObjectName("mainMenu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.fourPlayerStart.setText(QtGui.QApplication.translate("MainWindow", "4 Player Start", None, QtGui.QApplication.UnicodeUTF8))
        self.mainMenu.setText(QtGui.QApplication.translate("MainWindow", "Main Menu", None, QtGui.QApplication.UnicodeUTF8))

