# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 636)
        Dialog.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 91, 41))
        self.label.setStyleSheet(u"color:rgb(225, 225, 225); font-size:28pt;")
        self.fname = QLineEdit(Dialog)
        self.fname.setObjectName(u"fname")
        self.fname.setGeometry(QRect(190, 140, 191, 31))
        self.fname.setStyleSheet(u"font-size:14pt; color:rgb(243, 243, 243)")
        self.lname = QLineEdit(Dialog)
        self.lname.setObjectName(u"lname")
        self.lname.setGeometry(QRect(190, 210, 191, 31))
        self.lname.setStyleSheet(u"font-size:14pt; color:rgb(243, 243, 243)")
        self.label2 = QLabel(Dialog)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(60, 140, 121, 21))
        self.label2.setStyleSheet(u"font-size:18pt; color:rgb(225, 225, 225);")
        self.label3 = QLabel(Dialog)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(60, 210, 121, 21))
        self.label3.setStyleSheet(u"font-size:18pt;color:rgb(225, 225, 225);")
        self.loginbutton = QPushButton(Dialog)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(180, 560, 141, 51))
        self.loginbutton.setStyleSheet(u"background-color: rgb(167, 168, 167); font-size:14pt; color:rgb(255, 255, 255)")
        self.label3_2 = QLabel(Dialog)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setGeometry(QRect(60, 280, 121, 21))
        self.label3_2.setStyleSheet(u"font-size:18pt;color:rgb(225, 225, 225);")
        self.address = QLineEdit(Dialog)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(190, 280, 191, 31))
        self.address.setStyleSheet(u"font-size:14pt; color:rgb(243, 243, 243)")
        self.label3_3 = QLabel(Dialog)
        self.label3_3.setObjectName(u"label3_3")
        self.label3_3.setGeometry(QRect(60, 350, 121, 21))
        self.label3_3.setStyleSheet(u"font-size:18pt;color:rgb(225, 225, 225);")
        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(190, 350, 191, 31))
        self.username.setStyleSheet(u"font-size:14pt; color:rgb(243, 243, 243)")
        self.label3_4 = QLabel(Dialog)
        self.label3_4.setObjectName(u"label3_4")
        self.label3_4.setGeometry(QRect(30, 420, 151, 21))
        self.label3_4.setStyleSheet(u"font-size:18pt;color:rgb(225, 225, 225);")
        self.phone = QLineEdit(Dialog)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(190, 420, 191, 31))
        self.phone.setStyleSheet(u"font-size:14pt; color:rgb(243, 243, 243)")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.loginbutton.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.label3_2.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label3_3.setText(QCoreApplication.translate("Dialog", u"UserName", None))
        self.label3_4.setText(QCoreApplication.translate("Dialog", u"PhoneNumber", None))
        self.phone.setText("")
    # retranslateUi

