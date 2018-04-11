# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailView.ui'
#
# Created: Wed Apr 11 11:52:38 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_detailView(object):
    def setupUi(self, detailView):
        detailView.setObjectName("detailView")
        detailView.resize(789, 508)
        self.frame_playerInfo = QtGui.QFrame(detailView)
        self.frame_playerInfo.setGeometry(QtCore.QRect(0, 10, 471, 141))
        self.frame_playerInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_playerInfo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_playerInfo.setObjectName("frame_playerInfo")
        self.label_currPlayerName_2 = QtGui.QLabel(self.frame_playerInfo)
        self.label_currPlayerName_2.setGeometry(QtCore.QRect(10, 10, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_currPlayerName_2.setFont(font)
        self.label_currPlayerName_2.setScaledContents(False)
        self.label_currPlayerName_2.setObjectName("label_currPlayerName_2")
        self.label_playerInfo_2 = QtGui.QLabel(self.frame_playerInfo)
        self.label_playerInfo_2.setGeometry(QtCore.QRect(10, 30, 271, 101))
        self.label_playerInfo_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_playerInfo_2.setObjectName("label_playerInfo_2")
        self.button_closeDetail = QtGui.QPushButton(self.frame_playerInfo)
        self.button_closeDetail.setEnabled(True)
        self.button_closeDetail.setGeometry(QtCore.QRect(290, 80, 161, 51))
        self.button_closeDetail.setAutoFillBackground(False)
        self.button_closeDetail.setObjectName("button_closeDetail")

        self.retranslateUi(detailView)
        QtCore.QMetaObject.connectSlotsByName(detailView)

    def retranslateUi(self, detailView):
        detailView.setWindowTitle(QtGui.QApplication.translate("detailView", "Property Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_currPlayerName_2.setText(QtGui.QApplication.translate("detailView", "Player  :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playerInfo_2.setText(QtGui.QApplication.translate("detailView", "Player Info...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_closeDetail.setText(QtGui.QApplication.translate("detailView", "Close Detail View", None, QtGui.QApplication.UnicodeUTF8))

