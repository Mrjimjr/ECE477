# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameUi.ui'
#
# Created: Tue Apr 10 18:55:09 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_fourPlayerStart = QtGui.QPushButton(self.centralwidget)
        self.button_fourPlayerStart.setGeometry(QtCore.QRect(410, 340, 241, 71))
        self.button_fourPlayerStart.setObjectName("button_fourPlayerStart")
        self.frame_currentPlayerInfo = QtGui.QFrame(self.centralwidget)
        self.frame_currentPlayerInfo.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.frame_currentPlayerInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_currentPlayerInfo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_currentPlayerInfo.setObjectName("frame_currentPlayerInfo")
        self.label_currPlayerName = QtGui.QLabel(self.frame_currentPlayerInfo)
        self.label_currPlayerName.setGeometry(QtCore.QRect(10, 10, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_currPlayerName.setFont(font)
        self.label_currPlayerName.setScaledContents(False)
        self.label_currPlayerName.setObjectName("label_currPlayerName")
        self.button_mainMenu = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_mainMenu.setGeometry(QtCore.QRect(1140, 10, 121, 31))
        self.button_mainMenu.setObjectName("button_mainMenu")
        self.button_movePlayer = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_movePlayer.setEnabled(True)
        self.button_movePlayer.setGeometry(QtCore.QRect(110, 190, 241, 71))
        self.button_movePlayer.setAutoFillBackground(False)
        self.button_movePlayer.setObjectName("button_movePlayer")
        self.button_nextPlayer = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_nextPlayer.setEnabled(False)
        self.button_nextPlayer.setGeometry(QtCore.QRect(350, 190, 241, 71))
        self.button_nextPlayer.setObjectName("button_nextPlayer")
        self.frame_Player1 = QtGui.QFrame(self.frame_currentPlayerInfo)
        self.frame_Player1.setGeometry(QtCore.QRect(340, 500, 491, 141))
        self.frame_Player1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Player1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Player1.setObjectName("frame_Player1")
        self.frame_Player1_2 = QtGui.QFrame(self.frame_currentPlayerInfo)
        self.frame_Player1_2.setGeometry(QtCore.QRect(630, 210, 491, 141))
        self.frame_Player1_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Player1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Player1_2.setObjectName("frame_Player1_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_fourPlayerStart.setText(QtGui.QApplication.translate("MainWindow", "4 Player Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_currPlayerName.setText(QtGui.QApplication.translate("MainWindow", "Player  :", None, QtGui.QApplication.UnicodeUTF8))
        self.button_mainMenu.setText(QtGui.QApplication.translate("MainWindow", "Main Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.button_movePlayer.setText(QtGui.QApplication.translate("MainWindow", "Roll Dice", None, QtGui.QApplication.UnicodeUTF8))
        self.button_nextPlayer.setText(QtGui.QApplication.translate("MainWindow", "End Turn", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

