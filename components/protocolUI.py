# -*- coding:utf-8 -*-

__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from resource.protocol import Ui_Form


class ProtocolPage(QMainWindow, Ui_Form):
    """协议窗体"""

    def __init__(self, parent=None, *args, **kwargs):
        super(ProtocolPage, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ProtocolPage()
    win.show()
    sys.exit(app.exec_())
