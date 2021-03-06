# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created: Thu Apr 12 18:29:22 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(1280, 727)
        self.frame_gold = QtGui.QFrame(mainMenu)
        self.frame_gold.setGeometry(QtCore.QRect(0, 0, 280, 1000))
        self.frame_gold.setStyleSheet("background-color: rgb(202, 186, 12)")
        self.frame_black = QtGui.QFrame(mainMenu)
        self.frame_black.lower()
        self.frame_black.setGeometry(QtCore.QRect(275, 0, 1000, 1000))
        self.frame_black.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.frame_newPlayer = QtGui.QFrame(mainMenu)
        self.frame_newPlayer.setGeometry(QtCore.QRect(290, 90, 461, 331))
        self.frame_newPlayer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_newPlayer.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_newPlayer.setObjectName("frame_newPlayer")
        self.line_top = QtGui.QFrame(self.frame_newPlayer)
        self.line_top.setGeometry(QtCore.QRect(10, 30, 441, 16))
        self.line_top.setLineWidth(2)
        self.line_top.setFrameShape(QtGui.QFrame.HLine)
        self.line_top.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_top.setObjectName("line_top")
        self.button_addPlayer = QtGui.QPushButton(self.frame_newPlayer)
        self.button_addPlayer.setGeometry(QtCore.QRect(10, 240, 441, 81))
        self.button_addPlayer.setObjectName("button_addPlayer")
        self.label_player1 = QtGui.QLabel(self.frame_newPlayer)
        self.label_player1.setGeometry(QtCore.QRect(20, 50, 66, 17))
        self.label_player1.setObjectName("label_player1")
        self.button_player1Color = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player1Color.setGeometry(QtCore.QRect(170, 40, 41, 41))
        self.button_player1Color.setText("")
        self.button_player1Color.setObjectName("button_player1Color")
        self.button_player1Piece = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player1Piece.setGeometry(QtCore.QRect(310, 40, 41, 41))
        self.button_player1Piece.setText("")
        self.button_player1Piece.setObjectName("button_player1Piece")
        self.label_player2 = QtGui.QLabel(self.frame_newPlayer)
        self.label_player2.setGeometry(QtCore.QRect(20, 100, 66, 17))
        self.label_player2.setObjectName("label_player2")
        self.button_player2Piece = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player2Piece.setGeometry(QtCore.QRect(310, 90, 41, 41))
        self.button_player2Piece.setText("")
        self.button_player2Piece.setObjectName("button_player2Piece")
        self.button_player2Color = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player2Color.setGeometry(QtCore.QRect(170, 90, 41, 41))
        self.button_player2Color.setText("")
        self.button_player2Color.setObjectName("button_player2Color")
        self.button_player3Piece = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player3Piece.setGeometry(QtCore.QRect(310, 140, 41, 41))
        self.button_player3Piece.setText("")
        self.button_player3Piece.setObjectName("button_player3Piece")
        self.label_player3 = QtGui.QLabel(self.frame_newPlayer)
        self.label_player3.setGeometry(QtCore.QRect(20, 150, 66, 17))
        self.label_player3.setObjectName("label_player3")
        self.button_player3Color = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player3Color.setGeometry(QtCore.QRect(170, 140, 41, 41))
        self.button_player3Color.setText("")
        self.button_player3Color.setObjectName("button_player3Color")
        self.label_player4 = QtGui.QLabel(self.frame_newPlayer)
        self.label_player4.setGeometry(QtCore.QRect(20, 200, 66, 17))
        self.label_player4.setObjectName("label_player4")
        self.button_player4Piece = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player4Piece.setGeometry(QtCore.QRect(310, 190, 41, 41))
        self.button_player4Piece.setText("")
        self.button_player4Piece.setObjectName("button_player4Piece")
        self.button_player4Color = QtGui.QPushButton(self.frame_newPlayer)
        self.button_player4Color.setGeometry(QtCore.QRect(170, 190, 41, 41))
        self.button_player4Color.setText("")
        self.button_player4Color.setObjectName("button_player4Color")
        self.layoutWidget = QtGui.QWidget(self.frame_newPlayer)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 421, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_playersTitle_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_playersTitle_3.setFont(font)
        self.label_playersTitle_3.setObjectName("label_playersTitle_3")
        self.horizontalLayout.addWidget(self.label_playersTitle_3)
        self.label_playersTitle = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_playersTitle.setFont(font)
        self.label_playersTitle.setObjectName("label_playersTitle")
        self.horizontalLayout.addWidget(self.label_playersTitle)
        self.label_playersTitle_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_playersTitle_2.setFont(font)
        self.label_playersTitle_2.setObjectName("label_playersTitle_2")
        self.horizontalLayout.addWidget(self.label_playersTitle_2)
        self.frame_colorPicker = QtGui.QFrame(mainMenu)
        self.frame_colorPicker.setGeometry(QtCore.QRect(770, 90, 471, 331))
        self.frame_colorPicker.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_colorPicker.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_colorPicker.setObjectName("frame_colorPicker")
        self.line_top_2 = QtGui.QFrame(self.frame_colorPicker)
        self.line_top_2.setGeometry(QtCore.QRect(20, 30, 441, 16))
        self.line_top_2.setLineWidth(2)
        self.line_top_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_top_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_top_2.setObjectName("line_top_2")
        self.label_colorPicker = QtGui.QLabel(self.frame_colorPicker)
        self.label_colorPicker.setGeometry(QtCore.QRect(20, 10, 136, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_colorPicker.setFont(font)
        self.label_colorPicker.setObjectName("label_colorPicker")
        self.layoutWidget1 = QtGui.QWidget(self.frame_colorPicker)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 50, 441, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_color_1 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_1.sizePolicy().hasHeightForWidth())
        self.button_color_1.setSizePolicy(sizePolicy)
        self.button_color_1.setText("")
        self.button_color_1.setObjectName("button_color_1")
        self.gridLayout.addWidget(self.button_color_1, 0, 0, 1, 1)
        self.button_color_2 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_2.sizePolicy().hasHeightForWidth())
        self.button_color_2.setSizePolicy(sizePolicy)
        self.button_color_2.setText("")
        self.button_color_2.setObjectName("button_color_2")
        self.gridLayout.addWidget(self.button_color_2, 0, 1, 1, 1)
        self.button_color_3 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_3.sizePolicy().hasHeightForWidth())
        self.button_color_3.setSizePolicy(sizePolicy)
        self.button_color_3.setText("")
        self.button_color_3.setObjectName("button_color_3")
        self.gridLayout.addWidget(self.button_color_3, 0, 2, 1, 1)
        self.button_color_4 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_4.sizePolicy().hasHeightForWidth())
        self.button_color_4.setSizePolicy(sizePolicy)
        self.button_color_4.setText("")
        self.button_color_4.setObjectName("button_color_4")
        self.gridLayout.addWidget(self.button_color_4, 0, 3, 1, 1)
        self.button_color_5 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_5.sizePolicy().hasHeightForWidth())
        self.button_color_5.setSizePolicy(sizePolicy)
        self.button_color_5.setText("")
        self.button_color_5.setObjectName("button_color_5")
        self.gridLayout.addWidget(self.button_color_5, 1, 0, 1, 1)
        self.button_color_6 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_6.sizePolicy().hasHeightForWidth())
        self.button_color_6.setSizePolicy(sizePolicy)
        self.button_color_6.setText("")
        self.button_color_6.setObjectName("button_color_6")
        self.gridLayout.addWidget(self.button_color_6, 1, 1, 1, 1)
        self.button_color_7 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_7.sizePolicy().hasHeightForWidth())
        self.button_color_7.setSizePolicy(sizePolicy)
        self.button_color_7.setText("")
        self.button_color_7.setObjectName("button_color_7")
        self.gridLayout.addWidget(self.button_color_7, 1, 2, 1, 1)
        self.button_color_8 = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color_8.sizePolicy().hasHeightForWidth())
        self.button_color_8.setSizePolicy(sizePolicy)
        self.button_color_8.setText("")
        self.button_color_8.setObjectName("button_color_8")
        self.gridLayout.addWidget(self.button_color_8, 1, 3, 1, 1)
        self.splitter = QtGui.QSplitter(mainMenu)
        self.splitter.setGeometry(QtCore.QRect(20, 190, 251, 231))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.button_startGame = QtGui.QPushButton(self.splitter)
        self.button_startGame.setEnabled(False)
        self.button_startGame.setObjectName("button_startGame")
        self.button_resumeGame = QtGui.QPushButton(self.splitter)
        self.button_resumeGame.setEnabled(False)
        self.button_resumeGame.setVisible(False)
        self.button_resumeGame.setObjectName("button_resumeGame")
        self.frame_piecePicker = QtGui.QFrame(mainMenu)
        self.frame_piecePicker.setGeometry(QtCore.QRect(290, 430, 951, 181))
        self.frame_piecePicker.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_piecePicker.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_piecePicker.setObjectName("frame_piecePicker")
        self.line_top_3 = QtGui.QFrame(self.frame_piecePicker)
        self.line_top_3.setGeometry(QtCore.QRect(20, 30, 901, 16))
        self.line_top_3.setLineWidth(2)
        self.line_top_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_top_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_top_3.setObjectName("line_top_3")
        self.label_colorPicker_2 = QtGui.QLabel(self.frame_piecePicker)
        self.label_colorPicker_2.setGeometry(QtCore.QRect(20, 10, 136, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_colorPicker_2.setFont(font)
        self.label_colorPicker_2.setObjectName("label_colorPicker_2")
        self.widget = QtGui.QWidget(self.frame_piecePicker)
        self.widget.setGeometry(QtCore.QRect(30, 50, 891, 111))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_piecePicker_1 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_1.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_1.setSizePolicy(sizePolicy)
        self.button_piecePicker_1.setText("")
        self.button_piecePicker_1.setObjectName("button_piecePicker_1")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_1)
        self.button_piecePicker_2 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_2.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_2.setSizePolicy(sizePolicy)
        self.button_piecePicker_2.setText("")
        self.button_piecePicker_2.setObjectName("button_piecePicker_2")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_2)
        self.button_piecePicker_3 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_3.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_3.setSizePolicy(sizePolicy)
        self.button_piecePicker_3.setText("")
        self.button_piecePicker_3.setObjectName("button_piecePicker_3")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_3)
        self.button_piecePicker_4 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_4.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_4.setSizePolicy(sizePolicy)
        self.button_piecePicker_4.setText("")
        self.button_piecePicker_4.setObjectName("button_piecePicker_4")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_4)
        self.button_piecePicker_5 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_5.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_5.setSizePolicy(sizePolicy)
        self.button_piecePicker_5.setText("")
        self.button_piecePicker_5.setObjectName("button_piecePicker_5")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_5)
        self.button_piecePicker_6 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_6.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_6.setSizePolicy(sizePolicy)
        self.button_piecePicker_6.setText("")
        self.button_piecePicker_6.setObjectName("button_piecePicker_6")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_6)
        self.button_piecePicker_7 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_7.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_7.setSizePolicy(sizePolicy)
        self.button_piecePicker_7.setText("")
        self.button_piecePicker_7.setObjectName("button_piecePicker_7")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_7)
        self.button_piecePicker_8 = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_piecePicker_8.sizePolicy().hasHeightForWidth())
        self.button_piecePicker_8.setSizePolicy(sizePolicy)
        self.button_piecePicker_8.setText("")
        self.button_piecePicker_8.setObjectName("button_piecePicker_8")
        self.horizontalLayout_2.addWidget(self.button_piecePicker_8)
        self.button_createNewGame = QtGui.QPushButton(mainMenu)
        self.button_createNewGame.setEnabled(True)
        self.button_createNewGame.setGeometry(QtCore.QRect(20, 70, 251, 113))
        self.button_createNewGame.setObjectName("button_createNewGame")

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        mainMenu.setWindowTitle(QtGui.QApplication.translate("mainMenu", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.button_addPlayer.setText(QtGui.QApplication.translate("mainMenu", "Add Player", None, QtGui.QApplication.UnicodeUTF8))
        self.label_player1.setText(QtGui.QApplication.translate("mainMenu", "Player 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_player2.setText(QtGui.QApplication.translate("mainMenu", "Player 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_player3.setText(QtGui.QApplication.translate("mainMenu", "Player 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_player4.setText(QtGui.QApplication.translate("mainMenu", "Player 4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playersTitle_3.setText(QtGui.QApplication.translate("mainMenu", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playersTitle.setText(QtGui.QApplication.translate("mainMenu", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playersTitle_2.setText(QtGui.QApplication.translate("mainMenu", "Piece", None, QtGui.QApplication.UnicodeUTF8))
        self.label_colorPicker.setText(QtGui.QApplication.translate("mainMenu", "Pick Your Color", None, QtGui.QApplication.UnicodeUTF8))
        self.button_startGame.setText(QtGui.QApplication.translate("mainMenu", "Start Game", None, QtGui.QApplication.UnicodeUTF8))
        #self.button_resumeGame.setText(QtGui.QApplication.translate("mainMenu", "Resume Game", None, QtGui.QApplication.UnicodeUTF8))
        self.label_colorPicker_2.setText(QtGui.QApplication.translate("mainMenu", "Pick Your Piece", None, QtGui.QApplication.UnicodeUTF8))
        self.button_createNewGame.setText(QtGui.QApplication.translate("mainMenu", "Create New Game", None, QtGui.QApplication.UnicodeUTF8))

