# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 200)
        Form.setMinimumSize(QtCore.QSize(400, 200))
        Form.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 21))
        self.label.setStyleSheet("\n"
"font: 12pt \"方正舒体\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_ok = QtWidgets.QPushButton(Form)
        self.pushButton_ok.setGeometry(QtCore.QRect(140, 130, 101, 41))
        self.pushButton_ok.setCheckable(True)
        self.pushButton_ok.setChecked(True)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(270, 130, 101, 41))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Form)
        self.pushButton_ok.clicked.connect(Form.jump_to)
        self.pushButton_cancel.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "转到指定行"))
        self.label.setText(_translate("Form", "行号(L)："))
        self.pushButton_ok.setText(_translate("Form", "转到"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))

