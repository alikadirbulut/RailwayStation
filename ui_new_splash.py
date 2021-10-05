# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_splash.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_splashscreen(object):
    def setupUi(self, splashscreen):
        if not splashscreen.objectName():
            splashscreen.setObjectName(u"splashscreen")
        splashscreen.resize(677, 400)
        self.centralwidget = QWidget(splashscreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(56,58,89);\n"
"	color:rgb(220, 220, 220);\n"
"border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 50, 651, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color:rgb(254, 121, 199)\n"
"")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(130, 120, 361, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color:rgb(98, 114, 164)\n"
"")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 270, 621, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color:rgb(200, 200, 200);\n"
"	border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.557, x2:0.989, y2:0.5, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 83, 255, 255));\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(10, 300, 631, 31))
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color:rgb(98, 114, 164)\n"
"")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(210, 330, 631, 41))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color:rgb(98, 114, 164)\n"
"")
        self.label_credits.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        splashscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashscreen)

        QMetaObject.connectSlotsByName(splashscreen)
    # setupUi

    def retranslateUi(self, splashscreen):
        splashscreen.setWindowTitle(QCoreApplication.translate("splashscreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("splashscreen", u"<strong> RAILWAY </strong> STATION", None))
        self.label_description.setText(QCoreApplication.translate("splashscreen", u"<html><head/><body><p><span style=\" font-weight:600;\">TICKET</span> APP</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("splashscreen", u"<html><head/><body><p>loading...</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("splashscreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Creator</span>: Okan R\u0131za Er\u00f6ks\u00fcz</p></body></html>", None))
    # retranslateUi

