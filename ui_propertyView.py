# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertyView.ui'
#
# Created: Wed Apr 11 08:47:57 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_propertyView(object):
    def setupUi(self, propertyView):
        propertyView.setObjectName("propertyView")
        propertyView.resize(800, 600)
        propertyView.setWindowOpacity(0.75)
        self.centralwidget = QtGui.QWidget(propertyView)
        self.centralwidget.setObjectName("centralwidget")
        propertyView.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(propertyView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        propertyView.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(propertyView)
        self.statusbar.setObjectName("statusbar")
        propertyView.setStatusBar(self.statusbar)

        self.retranslateUi(propertyView)
        QtCore.QMetaObject.connectSlotsByName(propertyView)

    def retranslateUi(self, propertyView):
        propertyView.setWindowTitle(QtGui.QApplication.translate("propertyView", "Property Viewer", None, QtGui.QApplication.UnicodeUTF8))

