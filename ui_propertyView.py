# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertyView.ui'
#
# Created: Thu Apr 12 18:20:52 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_propertyView(object):
    def setupUi(self, propertyView):
        propertyView.setObjectName("propertyView")
        propertyView.resize(1280, 712)
        propertyView.setWindowOpacity(0.25)
        self.frame_currentPlayerInfo = QtGui.QFrame(propertyView)
        self.frame_currentPlayerInfo.setGeometry(QtCore.QRect(0, 20, 1280, 720))
        self.frame_currentPlayerInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_currentPlayerInfo.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_currentPlayerInfo.setObjectName("frame_currentPlayerInfo")
        self.frame_playerInfo = QtGui.QFrame(self.frame_currentPlayerInfo)
        self.frame_playerInfo.setGeometry(QtCore.QRect(10, 10, 471, 141))
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
        self.button_closeProperties = QtGui.QPushButton(self.frame_playerInfo)
        self.button_closeProperties.setEnabled(True)
        self.button_closeProperties.setGeometry(QtCore.QRect(290, 80, 161, 51))
        self.button_closeProperties.setAutoFillBackground(False)
        self.button_closeProperties.setObjectName("button_closeProperties")
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
        self.layoutWidget_3 = QtGui.QWidget(self.frame_currentPlayerInfo)
        self.layoutWidget_3.setGeometry(QtCore.QRect(560, 6, 631, 141))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_rr_1 = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rr_1.sizePolicy().hasHeightForWidth())
        self.button_rr_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_rr_1.setFont(font)
        self.button_rr_1.setObjectName("button_rr_1")
        self.horizontalLayout_5.addWidget(self.button_rr_1)
        self.button_rr_2 = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rr_2.sizePolicy().hasHeightForWidth())
        self.button_rr_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_rr_2.setFont(font)
        self.button_rr_2.setObjectName("button_rr_2")
        self.horizontalLayout_5.addWidget(self.button_rr_2)
        self.button_rr_3 = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rr_3.sizePolicy().hasHeightForWidth())
        self.button_rr_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_rr_3.setFont(font)
        self.button_rr_3.setObjectName("button_rr_3")
        self.horizontalLayout_5.addWidget(self.button_rr_3)
        self.button_rr_4 = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rr_4.sizePolicy().hasHeightForWidth())
        self.button_rr_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_rr_4.setFont(font)
        self.button_rr_4.setObjectName("button_rr_4")
        self.horizontalLayout_5.addWidget(self.button_rr_4)
        self.layoutWidget = QtGui.QWidget(self.frame_currentPlayerInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 1261, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.button_pro_1 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_1.sizePolicy().hasHeightForWidth())
        self.button_pro_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_1.setFont(font)
        self.button_pro_1.setObjectName("button_pro_1")
        self.horizontalLayout_1.addWidget(self.button_pro_1)
        self.button_pro_2 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_2.sizePolicy().hasHeightForWidth())
        self.button_pro_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_2.setFont(font)
        self.button_pro_2.setObjectName("button_pro_2")
        self.horizontalLayout_1.addWidget(self.button_pro_2)
        self.button_pro_3 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_3.sizePolicy().hasHeightForWidth())
        self.button_pro_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_3.setFont(font)
        self.button_pro_3.setObjectName("button_pro_3")
        self.horizontalLayout_1.addWidget(self.button_pro_3)
        self.button_pro_4 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_4.sizePolicy().hasHeightForWidth())
        self.button_pro_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_4.setFont(font)
        self.button_pro_4.setObjectName("button_pro_4")
        self.horizontalLayout_1.addWidget(self.button_pro_4)
        self.button_pro_5 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_5.sizePolicy().hasHeightForWidth())
        self.button_pro_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_5.setFont(font)
        self.button_pro_5.setObjectName("button_pro_5")
        self.horizontalLayout_1.addWidget(self.button_pro_5)
        self.button_pro_6 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_6.sizePolicy().hasHeightForWidth())
        self.button_pro_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_6.setFont(font)
        self.button_pro_6.setObjectName("button_pro_6")
        self.horizontalLayout_1.addWidget(self.button_pro_6)
        self.button_pro_7 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_7.sizePolicy().hasHeightForWidth())
        self.button_pro_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_7.setFont(font)
        self.button_pro_7.setObjectName("button_pro_7")
        self.horizontalLayout_1.addWidget(self.button_pro_7)
        self.button_pro_8 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_8.sizePolicy().hasHeightForWidth())
        self.button_pro_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_8.setFont(font)
        self.button_pro_8.setObjectName("button_pro_8")
        self.horizontalLayout_1.addWidget(self.button_pro_8)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_pro_9 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_9.sizePolicy().hasHeightForWidth())
        self.button_pro_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_9.setFont(font)
        self.button_pro_9.setObjectName("button_pro_9")
        self.horizontalLayout_3.addWidget(self.button_pro_9)
        self.button_pro_10 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_10.sizePolicy().hasHeightForWidth())
        self.button_pro_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_10.setFont(font)
        self.button_pro_10.setObjectName("button_pro_10")
        self.horizontalLayout_3.addWidget(self.button_pro_10)
        self.button_pro_11 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_11.sizePolicy().hasHeightForWidth())
        self.button_pro_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_11.setFont(font)
        self.button_pro_11.setObjectName("button_pro_11")
        self.horizontalLayout_3.addWidget(self.button_pro_11)
        self.button_pro_12 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_12.sizePolicy().hasHeightForWidth())
        self.button_pro_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_12.setFont(font)
        self.button_pro_12.setObjectName("button_pro_12")
        self.horizontalLayout_3.addWidget(self.button_pro_12)
        self.button_pro_13 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_13.sizePolicy().hasHeightForWidth())
        self.button_pro_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_13.setFont(font)
        self.button_pro_13.setObjectName("button_pro_13")
        self.horizontalLayout_3.addWidget(self.button_pro_13)
        self.button_pro_14 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_14.sizePolicy().hasHeightForWidth())
        self.button_pro_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_14.setFont(font)
        self.button_pro_14.setObjectName("button_pro_14")
        self.horizontalLayout_3.addWidget(self.button_pro_14)
        self.button_pro_15 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_15.sizePolicy().hasHeightForWidth())
        self.button_pro_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_15.setFont(font)
        self.button_pro_15.setObjectName("button_pro_15")
        self.horizontalLayout_3.addWidget(self.button_pro_15)
        self.button_pro_16 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_16.sizePolicy().hasHeightForWidth())
        self.button_pro_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_16.setFont(font)
        self.button_pro_16.setObjectName("button_pro_16")
        self.horizontalLayout_3.addWidget(self.button_pro_16)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_pro_17 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_17.sizePolicy().hasHeightForWidth())
        self.button_pro_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_17.setFont(font)
        self.button_pro_17.setObjectName("button_pro_17")
        self.horizontalLayout_4.addWidget(self.button_pro_17)
        self.button_pro_18 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_18.sizePolicy().hasHeightForWidth())
        self.button_pro_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_18.setFont(font)
        self.button_pro_18.setObjectName("button_pro_18")
        self.horizontalLayout_4.addWidget(self.button_pro_18)
        self.button_pro_19 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_19.sizePolicy().hasHeightForWidth())
        self.button_pro_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_19.setFont(font)
        self.button_pro_19.setObjectName("button_pro_19")
        self.horizontalLayout_4.addWidget(self.button_pro_19)
        self.button_pro_20 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_20.sizePolicy().hasHeightForWidth())
        self.button_pro_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_20.setFont(font)
        self.button_pro_20.setObjectName("button_pro_20")
        self.horizontalLayout_4.addWidget(self.button_pro_20)
        self.button_pro_21 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_21.sizePolicy().hasHeightForWidth())
        self.button_pro_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_21.setFont(font)
        self.button_pro_21.setObjectName("button_pro_21")
        self.horizontalLayout_4.addWidget(self.button_pro_21)
        self.button_pro_22 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_22.sizePolicy().hasHeightForWidth())
        self.button_pro_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_22.setFont(font)
        self.button_pro_22.setObjectName("button_pro_22")
        self.horizontalLayout_4.addWidget(self.button_pro_22)
        self.button_pro_23 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_23.sizePolicy().hasHeightForWidth())
        self.button_pro_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_23.setFont(font)
        self.button_pro_23.setObjectName("button_pro_23")
        self.horizontalLayout_4.addWidget(self.button_pro_23)
        self.button_pro_24 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pro_24.sizePolicy().hasHeightForWidth())
        self.button_pro_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.button_pro_24.setFont(font)
        self.button_pro_24.setObjectName("button_pro_24")
        self.horizontalLayout_4.addWidget(self.button_pro_24)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(propertyView)
        QtCore.QMetaObject.connectSlotsByName(propertyView)

    def retranslateUi(self, propertyView):
        propertyView.setWindowTitle(QtGui.QApplication.translate("propertyView", "Property Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_currPlayerName_2.setText(QtGui.QApplication.translate("propertyView", "Player  :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_playerInfo_2.setText(QtGui.QApplication.translate("propertyView", "Player Info...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_closeProperties.setText(QtGui.QApplication.translate("propertyView", "Close My Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rr_1.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rr_2.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rr_3.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rr_4.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_1.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_2.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_3.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_4.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_5.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_6.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_7.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_8.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_9.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_10.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_11.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_12.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_13.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_14.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_15.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_16.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_17.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_18.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_19.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_20.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_21.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_22.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_23.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pro_24.setText(QtGui.QApplication.translate("propertyView", "<<Prop Name>>\n"
"\n"
"\n"
"\n"
">", None, QtGui.QApplication.UnicodeUTF8))

