# -*- coding:utf-8 -*-

__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIntValidator

from resource.transto import Ui_Form

class LineValidator(QIntValidator):
    """自定义验证器，仅允许输入数字"""

    def fixup(self,p_str):
        """当输入结束时仍处于中间状态时，有一次修复结果的机会"""
        if p_str=='' or int(p_str)<self.bottom():
            return ''

class TransToPage(QMainWindow,Ui_Form):
    """转到窗体"""

    # 发送行号的信号
    transto_signal = pyqtSignal(str)

    def __init__(self,parent=None,*args,**kwargs):
        super(TransToPage, self).__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.lineEdit.setValidator(LineValidator(1,9999,self.lineEdit))

    def jump_to(self):
        #print('转到')
        if self.lineEdit.text():
            self.transto_signal.emit(self.lineEdit.text())
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TransToPage()
    win.show()
    sys.exit(app.exec_())