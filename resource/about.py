# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 500)
        Form.setMinimumSize(QtCore.QSize(520, 500))
        Form.setMaximumSize(QtCore.QSize(520, 500))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(430, 460, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 520, 241))
        self.label.setMinimumSize(QtCore.QSize(520, 200))
        self.label.setMaximumSize(QtCore.QSize(520, 300))
        self.label.setStyleSheet("background-image: url(:/icon/about.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 360, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 380, 121, 21))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 320, 321, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("border:none;\n"
"text-decoration : underline ;\n"
"color:rgb(60, 102, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(Form.show_protocol)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于\"记事本\""))
        self.pushButton.setText(_translate("Form", "确认"))
        self.label_4.setText(_translate("Form", "个人用户"))
        self.label_5.setText(_translate("Form", "微软中国"))
        self.label_2.setText(_translate("Form", "根据"))
        self.pushButton_2.setText(_translate("Form", "Microsoft 软件许可条款"))
        self.label_3.setText(_translate("Form", "，许可如下用户使用本产品："))

import notepadqrc_rc
