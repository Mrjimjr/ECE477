# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailView.ui'
#
# Created: Wed Apr 11 23:52:30 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_detailView(object):
    def setupUi(self, detailView):
        detailView.setObjectName("detailView")
        detailView.resize(1036, 632)
        self.frame = QtGui.QFrame(detailView)
        self.frame_background = QtGui.QFrame(detailView)
        self.frame_background.setGeometry(QtCore.QRect(0, 0, 1261, 800))
        self.frame_background.setStyleSheet("")
        self.frame_background.lower()
        self.label_topColor = QtGui.QLabel(detailView)
        self.label_topColor.setGeometry(QtCore.QRect(150, 110, 510, 65))
        self.label_topColor.setStyleSheet("background-color: rgb(202, 186, 12)")
        self.frame.setGeometry(QtCore.QRect(150, 175, 510, 450))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setObjectName("frame")
        self.propIcon = QtGui.QPushButton(self.frame)
        self.propIcon.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.propIcon.setText("")
        self.propIcon.setObjectName("propIcon")
        self.label_propText = QtGui.QLabel(self.frame)
        self.label_propText.setGeometry(QtCore.QRect(40, 220, 421, 150))
        self.label_propText.setWordWrap(True)
        self.label_propText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propText.setObjectName("label_propText")
        #self.label_propText.setStyleS
        self.button_closeDetail = QtGui.QPushButton(detailView)
        self.button_closeDetail.setEnabled(True)
        self.button_closeDetail.setGeometry(QtCore.QRect(583, 185, 70, 50))
        self.button_closeDetail.setAutoFillBackground(False)
        self.button_closeDetail.setObjectName("button_closeDetail")
        self.button_upgrade = QtGui.QPushButton(self.frame)
        self.button_upgrade.setEnabled(True)
        self.button_upgrade.setGeometry(QtCore.QRect(480, 250, 90, 70))
        self.button_upgrade.setAutoFillBackground(False)
        self.button_upgrade.setObjectName("button_upgrade")
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(220, 20, 291, 191))
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
        
        self.label_propOwner = QtGui.QLabel(self.widget)
        self.label_propOwner.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propOwner.setObjectName("label_propOwner")
        self.verticalLayout.addWidget(self.label_propOwner)
        
        
        self.label_propCost = QtGui.QLabel(self.widget)
        self.label_propCost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_propCost.setObjectName("label_propCost")
        self.verticalLayout.addWidget(self.label_propCost)

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
        self.button_upgrade.setText(QtGui.QApplication.translate("detailView", "Upgrade", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propName.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propCost.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propOwner.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propRent.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpCost.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpRent.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_propUpText.setText(QtGui.QApplication.translate("detailView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

