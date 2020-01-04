# -*- coding:utf-8 -*-
__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal

from resource.replace import Ui_Form

class ReplacePage(QMainWindow,Ui_Form):
    """替换窗体"""

    finder_signal = pyqtSignal(str,bool,bool)
    replacestr_signal = pyqtSignal(str,str,bool,bool)
    replaceall_signal = pyqtSignal(str,str,bool)

    def __init__(self,parent=None,*args,**kwargs):
        super(ReplacePage, self).__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.lineEdit.setFocus()

    def findnext(self):
        """查找下一个"""
        findtext = self.lineEdit.text()
        if findtext:
            sensitive_case = self.checkBox.isChecked()
            loop = self.checkBox_2.isChecked()
            self.finder_signal.emit(findtext,sensitive_case,loop)

    def replacestr(self):
        """替换"""
        findtext = self.lineEdit.text()
        replacetext = self.lineEdit_2.text()
        if findtext:
            sensitive_case = self.checkBox.isChecked()
            loop = self.checkBox_2.isChecked()
            self.replacestr_signal.emit(findtext,replacetext, sensitive_case, loop)

    def replaceall(self):
        """替换所有"""
        findtext = self.lineEdit.text()
        replacetext = self.lineEdit_2.text()
        if findtext:
            sensitive_case = self.checkBox.isChecked()
            self.replaceall_signal.emit(findtext,replacetext, sensitive_case)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ReplacePage()
    win.show()
    sys.exit(app.exec_())