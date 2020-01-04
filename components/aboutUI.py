# -*- coding:utf-8 -*-

__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from resource.about import Ui_Form
from components.protocolUI import ProtocolPage

class AboutPage(QMainWindow,Ui_Form):
    """关于页面"""

    def __init__(self,parent=None,*args,**kwargs):
        super(AboutPage, self).__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.protocol = ProtocolPage(self)

    def show_protocol(self):
        """展示协议"""
        #print("展示协议")
        self.protocol.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AboutPage()
    win.show()
    sys.exit(app.exec_())