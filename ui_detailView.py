# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailView.ui'
#
# Created: Wed Apr 11 13:21:05 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_detailView(object):
    def setupUi(self, detailView):
        detailView.setObjectName("detailView")
        detailView.resize(1036, 632)
        self.frame = QtGui.QFrame(detailView)
        self.frame.setGeometry(QtCore.QRect(280, 130, 551, 331))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setObjectName("frame")
        self.propIcon = QtGui.QPushButton(self.frame)
        self.propIcon.setGeometry(QtCore.QRect(10, 10, 151, 201))
        self.propIcon.setText("")
        self.propIcon.setObjectName("propIcon")
        self.label_propText = QtGui.QLabel(self.frame)
        self.label_propText.setGeometry(QtCore.QRect(20, 220, 421, 91))
        self.label_propText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propText.setObjectName("label_propText")
        self.button_closeDetail = QtGui.QPushButton(self.frame)
        self.button_closeDetail.setEnabled(True)
        self.button_closeDetail.setGeometry(QtCore.QRect(470, 20, 71, 51))
        self.button_closeDetail.setAutoFillBackground(False)
        self.button_closeDetail.setObjectName("button_closeDetail")
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(170, 20, 291, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_propName = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_propName.setFont(font)
        self.label_propName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propName.setObjectName("label_propName")
        self.verticalLayout.addWidget(self.label_propName)
        self.label_propCost = QtGui.QLabel(self.widget)
        self.label_propCost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propCost.setObjectName("label_propCost")
        self.verticalLayout.addWidget(self.label_propCost)
        self.label_propOwner = QtGui.QLabel(self.widget)
        self.label_propOwner.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propOwner.setObjectName("label_propOwner")
        self.verticalLayout.addWidget(self.label_propOwner)
        self.label_propRent = QtGui.QLabel(self.widget)
        self.label_propRent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propRent.setObjectName("label_propRent")
        self.verticalLayout.addWidget(self.label_propRent)
        self.label_propUpCost = QtGui.QLabel(self.widget)
        self.label_propUpCost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propUpCost.setObjectName("label_propUpCost")
        self.verticalLayout.addWidget(self.label_propUpCost)
        self.label_propUpRent = QtGui.QLabel(self.widget)
        self.label_propUpRent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propUpRent.setObjectName("label_propUpRent")
        self.verticalLayout.addWidget(self.label_propUpRent)
        self.label_propUpText = QtGui.QLabel(self.widget)
        self.label_propUpText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propUpText.setObjectName("label_propUpText")
        self.verticalLayout.addWidget(self.label_propUpText)

        self.retranslateUi(detailView)
        QtCore.QMetaObject.connectSlotsByName(detailView)

    def retranslateUi(self, detailView):
        detailView.setWindowTitle(QtGui.QApplication.translate("detailView", "Property Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propText.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_closeDetail.setText(QtGui.QApplication.translate("detailView", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propName.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propCost.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propOwner.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propRent.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpCost.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpRent.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpText.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

