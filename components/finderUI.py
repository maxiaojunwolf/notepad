# -*- coding:utf-8 -*-

__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal

from resource.finder import Ui_Form

class FindPage(QMainWindow,Ui_Form):
    """查找页面"""

    # 发送输入结果信号给主页面
    finder_signal = pyqtSignal(str,bool,bool,bool)

    def __init__(self,parent=None,*args,**kwargs):
        super(FindPage, self).__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.lineEdit.setFocus()

    def findstr(self):
        """查找"""
        text = self.lineEdit.text()
        if text:
            sensitive_case = self.checkBox.isChecked()
            loop = self.checkBox_2.isChecked()
            backward = self.radioButton.isChecked()
            self.finder_signal.emit(text,sensitive_case,loop,backward)

    def findnext(self):
        """查找下一个"""
        text = self.lineEdit.text()
        if text:
            sensitive_case = self.checkBox.isChecked()
            loop = self.checkBox_2.isChecked()
            backward = self.radioButton.isChecked()
            self.finder_signal.emit(text, sensitive_case, loop, backward)

    def findlast(self):
        """查找上一个"""
        text = self.lineEdit.text()
        if text:
            sensitive_case = self.checkBox.isChecked()
            loop = self.checkBox_2.isChecked()
            backward = not self.radioButton.isChecked()
            self.finder_signal.emit(text, sensitive_case, loop, backward)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FindPage()
    win.show()
    sys.exit(app.exec_())