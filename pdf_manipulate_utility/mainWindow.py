# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 763)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1051, 763))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("QPushButton#encrypt{\n"
"    \n"
"    background-color: rgb(6, 33, 50);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#encrypt:hover{\n"
"    background-color: rgb(13, 23, 65);\n"
"}\n"
"QPushButton#encrypt:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(6, 33, 50);\n"
"}\n"
"\n"
"QPushButton#merge{\n"
"    \n"
"    background-color: rgb(6, 33, 50);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#merge:hover{\n"
"    background-color: rgb(13, 23, 65);\n"
"}\n"
"QPushButton#merge:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(6, 33, 50);\n"
"}\n"
"border-radius: 5px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 431, 711))
        self.widget.setMouseTracking(True)
        self.widget.setStyleSheet("border-image: url(:/image/image/background.jpg);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 0, 661, 711))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 80);\n"
"border-bottom-right-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 80, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgb(240, 255, 240);\n"
"padding-bottom: 7px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 630, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgb(240, 255, 240);\n"
"padding-bottom: 7px;")
        self.label_3.setObjectName("label_3")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(520, 510, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.merge = QtWidgets.QPushButton(self.centralwidget)
        self.merge.setGeometry(QtCore.QRect(790, 510, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.merge.setFont(font)
        self.merge.setObjectName("merge")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConvert = QtWidgets.QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.del_metadata = QtWidgets.QAction(MainWindow)
        self.del_metadata.setObjectName("del_metadata")
        self.actionimage_to_pdf = QtWidgets.QAction(MainWindow)
        self.actionimage_to_pdf.setObjectName("actionimage_to_pdf")
        self.menuFile.addAction(self.actionConvert)
        self.menuFile.addAction(self.del_metadata)
        self.menuFile.addAction(self.actionimage_to_pdf)
        self.menuhelp.addAction(self.about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Select from top menu that\n"
" you want to do!"))
        self.label_3.setText(_translate("MainWindow", "PDF M a n i p u l a t e  Utility [BETA]"))
        self.encrypt.setText(_translate("MainWindow", "E n c r y p t _ P D F"))
        self.merge.setText(_translate("MainWindow", "M e r g e_PDF"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionConvert.setText(_translate("MainWindow", "Convert"))
        self.about.setText(_translate("MainWindow", "about"))
        self.del_metadata.setText(_translate("MainWindow", "del_metadata"))
        self.actionimage_to_pdf.setText(_translate("MainWindow", "image_to_pdf"))
import res_rc
