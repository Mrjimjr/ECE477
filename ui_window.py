# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameUi.ui'
#
# Created: Fri Apr 13 16:31:25 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 772)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_newGame = QtGui.QPushButton(self.centralwidget)
        self.button_newGame.setEnabled(True)
        self.button_newGame.setGeometry(QtCore.QRect(410, 340, 241, 71))
        self.button_newGame.setObjectName("button_newGame")
        self.frame_currentPlayerInfo = QtGui.QFrame(self.centralwidget)
        self.frame_currentPlayerInfo.setGeometry(QtCore.QRect(-40, 0, 1280, 720))
        self.frame_currentPlayerInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_currentPlayerInfo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_currentPlayerInfo.setObjectName("frame_currentPlayerInfo")
        self.button_mainMenu = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_mainMenu.setGeometry(QtCore.QRect(1140, 10, 121, 31))
        self.button_mainMenu.setObjectName("button_mainMenu")
        self.button_playerAction = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_playerAction.setEnabled(True)
        self.button_playerAction.setGeometry(QtCore.QRect(740, 590, 241, 71))
        self.button_playerAction.setAutoFillBackground(False)
        self.button_playerAction.setObjectName("button_playerAction")
        self.button_nextPlayer = QtGui.QPushButton(self.frame_currentPlayerInfo)
        self.button_nextPlayer.setEnabled(False)
        self.button_nextPlayer.setGeometry(QtCore.QRect(980, 590, 241, 71))
        self.button_nextPlayer.setObjectName("button_nextPlayer")
        self.frame_playerInfo = QtGui.QFrame(self.frame_currentPlayerInfo)
        self.frame_playerInfo.setGeometry(QtCore.QRect(10, 10, 471, 141))
        self.frame_playerInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_playerInfo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_playerInfo.setObjectName("frame_playerInfo")
        self.label_currPlayerName = QtGui.QLabel(self.frame_playerInfo)
        self.label_currPlayerName.setGeometry(QtCore.QRect(10, 10, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_currPlayerName.setFont(font)
        self.label_currPlayerName.setScaledContents(False)
        self.label_currPlayerName.setObjectName("label_currPlayerName")
        self.label_playerInfo = QtGui.QLabel(self.frame_playerInfo)
        self.label_playerInfo.setGeometry(QtCore.QRect(10, 30, 271, 101))
        self.label_playerInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_playerInfo.setObjectName("label_playerInfo")
        self.button_showProperties = QtGui.QPushButton(self.frame_playerInfo)
        self.button_showProperties.setEnabled(False)
        self.button_showProperties.setGeometry(QtCore.QRect(290, 80, 161, 51))
        self.button_showProperties.setAutoFillBackground(False)
        self.button_showProperties.setObjectName("button_showProperties")
        self.button_playerColorInd = QtGui.QPushButton(self.frame_playerInfo)
        self.button_playerColorInd.setEnabled(False)
        self.button_playerColorInd.setGeometry(QtCore.QRect(290, 10, 71, 61))
        self.button_playerColorInd.setAutoFillBackground(False)
        self.button_playerColorInd.setText("")
        self.button_playerColorInd.setObjectName("button_playerColorInd")
        self.button_button_playerPieceInd = QtGui.QPushButton(self.frame_playerInfo)
        self.button_button_playerPieceInd.setEnabled(False)
        self.button_button_playerPieceInd.setGeometry(QtCore.QRect(370, 10, 71, 61))
        self.button_button_playerPieceInd.setAutoFillBackground(False)
        self.button_button_playerPieceInd.setText("")
        self.button_button_playerPieceInd.setObjectName("button_button_playerPieceInd")
        self.frame_diceResult = QtGui.QFrame(self.frame_currentPlayerInfo)
        self.frame_diceResult.setGeometry(QtCore.QRect(740, 460, 481, 121))
        self.frame_diceResult.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_diceResult.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_diceResult.setObjectName("frame_diceResult")
        self.label_diceTitle = QtGui.QLabel(self.frame_diceResult)
        self.label_diceTitle.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_diceTitle.setObjectName("label_diceTitle")
        self.label_Dice1 = QtGui.QLabel(self.frame_diceResult)
        self.label_Dice1.setGeometry(QtCore.QRect(110, 100, 66, 17))
        self.label_Dice1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Dice1.setObjectName("label_Dice1")
        self.label_Dice2 = QtGui.QLabel(self.frame_diceResult)
        self.label_Dice2.setGeometry(QtCore.QRect(230, 100, 66, 17))
        self.label_Dice2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Dice2.setObjectName("label_Dice2")
        self.label_diceTotal = QtGui.QLabel(self.frame_diceResult)
        self.label_diceTotal.setGeometry(QtCore.QRect(360, 100, 66, 17))
        self.label_diceTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diceTotal.setObjectName("label_diceTotal")
        self.label_diceTotalImage = QtGui.QLabel(self.frame_diceResult)
        self.label_diceTotalImage.setGeometry(QtCore.QRect(350, 10, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_diceTotalImage.setFont(font)
        self.label_diceTotalImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diceTotalImage.setObjectName("label_diceTotalImage")
        self.button_dice1Image = QtGui.QPushButton(self.frame_diceResult)
        self.button_dice1Image.setGeometry(QtCore.QRect(100, 10, 81, 81))
        self.button_dice1Image.setObjectName("button_dice1Image")
        self.button_dice2Image = QtGui.QPushButton(self.frame_diceResult)
        self.button_dice2Image.setGeometry(QtCore.QRect(220, 10, 81, 81))
        self.button_dice2Image.setObjectName("button_dice2Image")
        self.spotImage = QtGui.QWidget(self.frame_currentPlayerInfo)
        self.spotImage.setGeometry(QtCore.QRect(130, 230, 411, 371))
        self.spotImage.setObjectName("spotImage")
        self.spotText = QtGui.QLabel(self.frame_currentPlayerInfo)
        self.spotText.setGeometry(QtCore.QRect(740, 100, 461, 231))
        self.spotText.setText("")
        self.spotText.setObjectName("spotText")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.button_newGame.setText(QtGui.QApplication.translate("MainWindow", "Create New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.button_mainMenu.setText(QtGui.QApplication.translate("MainWindow", "Main Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.button_playerAction.setText(QtGui.QApplication.translate("MainWindow", "Roll Dice", None, QtGui.QApplication.UnicodeUTF8))
        self.button_nextPlayer.setText(QtGui.QApplication.translate("MainWindow", "End Turn", None, QtGui.QApplication.UnicodeUTF8))
        self.label_currPlayerName.setText(QtGui.QApplication.translate("MainWindow", "Player  :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playerInfo.setText(QtGui.QApplication.translate("MainWindow", "Player Info...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_showProperties.setText(QtGui.QApplication.translate("MainWindow", "Show My Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_diceTitle.setText(QtGui.QApplication.translate("MainWindow", "Roll Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Dice1.setText(QtGui.QApplication.translate("MainWindow", "Dice 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Dice2.setText(QtGui.QApplication.translate("MainWindow", "Dice 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_diceTotal.setText(QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_diceTotalImage.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.button_dice1Image.setText(QtGui.QApplication.translate("MainWindow", "<Dice 1>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_dice2Image.setText(QtGui.QApplication.translate("MainWindow", "<Dice 2>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

