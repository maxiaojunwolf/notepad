# -*- coding:utf-8 -*-
import os
import re
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QUrl
# QTextDocument导入别删，查询时用到
from PyQt5.QtGui import QDesktopServices, QTextCursor, QTextDocument
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

from components.aboutUI import AboutPage
from components.finderUI import FindPage
from components.replaceUI import ReplacePage
from components.transtoUI import TransToPage
from resource.notepad import Ui_MainWindow

__author__ = 'mxj'
__date__ = '2019/8/28 15:00'

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox, QTextEdit, QFontDialog, \
    QColorDialog, QLabel, QMenu, QAction


class NotePad(QMainWindow, Ui_MainWindow):
    """仿windows记事本"""

    # 默认未保存时的title
    DEFAULTNAME = '无标题'
    # 默认titl后缀
    DEFAULTSUFFIX = '记事本'
    # 默认搜索url
    SEARCHURL = 'https://cn.bing.com'
    # 状态栏格式
    STATUS_MSG = '|  第{}行，第{}列  |  {}  |  Windows(CRLF)  |   UTF-8        '

    def __init__(self, parent=None, *args, **kwargs):
        super(NotePad, self).__init__(parent, *args, **kwargs)
        self.setupui()

    def setupui(self):
        """加载组件，绑定信号"""
        self.setupUi(self)
        self.initstate()
        # 查找窗体
        self.finderui = FindPage(self)
        # 转到窗体
        self.transtoui = TransToPage(self)
        # 替换窗体
        self.replaceui = ReplacePage(self)
        # 关于窗体
        self.aboutui = AboutPage(self)
        # 绑定信号获取用户输入的行号
        self.transtoui.transto_signal.connect(self.get_transto_line)
        # 获取查询条件
        self.finderui.finder_signal.connect(self.findstr)
        # 获取替换条件
        self.replaceui.finder_signal.connect(self.replace_findnext)
        self.replaceui.replacestr_signal.connect(self.replacestr)
        self.replaceui.replaceall_signal.connect(self.replaceall)
        # 鼠标位置变化实时更新底部状态栏
        self.textEdit.cursorPositionChanged.connect(self.positionchange)
        # 显示右键
        self.textEdit.customContextMenuRequested.connect(self.showContextMenu)
    def initstate(self):
        """初始化状态"""
        # 保存文件路径和文件名
        self.filepath = None
        self.filename = None
        # 记录缩放大小
        self.zoomin = 0
        # 默认复制剪贴删除状态为False
        self.action_T_Ctrl_X.setEnabled(False)
        self.action_C_Ctrl_C.setEnabled(False)
        self.action_L_Del.setEnabled(False)
        # 更新窗体标题
        self.update_windowtitle()
        # 内容置空
        self.textEdit.setText('')
        # 初始化状态栏
        self.init_statusbar()
        # 添加自定义右键操作
        self.addContextMenu()
    # --------------------新建菜单开始-----------------------------------------
    def newfile(self):
        """新建操作"""

        print('新建文件')
        # 询问保存
        self.query_save()
        # 重置初始状态
        self.initstate()

    def newwindow(self):
        """新窗口"""

        print('新建窗体')
        self.newwindow = NotePad()
        self.newwindow.show()

    def openfile(self):
        """打开文件"""
        print('打开文件')
        # 询问保存
        self.query_save()
        # 返回文件路径和所选的类型
        filepath, cancled = QFileDialog.getOpenFileName(self, '打开文件', '.', '文本文档(*.txt)\n所有文件(*.*)')
        if filepath:
            with open(filepath, 'r', encoding='UTF8', errors='ignore') as f:
                self.textEdit.setText(f.read())
            self.filepath = filepath
            self.filename = os.path.basename(filepath)
            self.update_windowtitle()

    def savefile(self):
        """保存操作"""

        print('保存文件')
        if self.filepath:
            self.savefile_()
        else:
            filepath = self.chose_savepath()
            if filepath:
                self.savefile_(filepath)

    def savefileas(self):
        """另存为操作"""

        print('另存为')
        filepath = self.chose_savepath()
        if filepath:
            self.savefile_(filepath, mode='SAVEAS')

    def setpage(self):
        """页面设置（这里与window有些差异）:结合了打印预览功能"""
        print('页面设置')
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePrint)
        dialog.exec_()

    def printfile(self):
        """打印"""
        print('打印文件')
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QDialog.Accepted:
            self.handlePrint(printer)

    def query_save(self):
        """询问是否保存"""
        if self.isunsaved():
            # 内容为空且未保存时不询问
            if (self.filepath is None) and self.textEdit.toPlainText() == '':
                return
            if self.query_ifsave():
                if self.filepath is None:
                    filepath = self.chose_savepath()
                    if filepath:
                        self.savefile_(filepath)
                else:
                    self.savefile_()

    def handlePrint(self, printer):
        """调用打印"""
        self.textEdit.print(printer)

    def exitfile(self):
        """退出"""
        print('退出')
        self.query_save()
        self.close()

    def query_ifsave(self):
        """点击保存或新建时，询问保存"""
        messageBox = QMessageBox()
        messageBox.setWindowTitle('记事本')
        messageBox.setText('你想将更改保存到 {} 吗？'.format(self.filename))
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText('保存(S)')
        buttonN = messageBox.button(QMessageBox.No)
        buttonN.setText('不保存(N)')
        buttonN = messageBox.button(QMessageBox.Cancel)
        buttonN.setText('取消')
        messageBox.exec_()
        if messageBox.clickedButton() == buttonY:
            return True

    def chose_savepath(self):
        """选择保存位置"""
        # 打开保存位置对话框
        filepath, cancled = QFileDialog.getSaveFileName(self, '另存为', '.', '文本文档(*.txt)\n所有文件(*.*)')
        return filepath

    def savefile_(self, filepath=None, mode='SAVE'):
        """保存文件"""
        if filepath is None:
            filepath = self.filepath
        else:
            if mode == 'SAVE':
                # 更新文件路径和文件名
                self.filepath = filepath
                self.filename = os.path.basename(filepath)
        with open(filepath, 'w', encoding='UTF8') as f:
            f.write(self.textEdit.toPlainText())
        self.update_windowtitle()

    # --------------------新建菜单结束-----------------------------------------


    # --------------------编辑菜单开始-----------------------------------------

    def revokeedit(self):
        """撤销"""
        print('撤销')
        self.textEdit.undo()

    def cutedit(self):
        """剪贴"""
        print('剪贴')
        self.textEdit.cut()

    def copyedit(self):
        """复制"""
        print('复制')
        self.textEdit.copy()

    def pasteredit(self):
        """粘贴"""
        print('粘贴')
        self.textEdit.paste()

    def deledit(self):
        """删除"""
        print('删除')
        self.textEdit.textCursor().removeSelectedText()

    def searchbybing(self):
        """使用bing搜索"""
        print('使用bing搜索')
        selected = self.textEdit.textCursor().selectedText()
        if selected == '':
            selected = self.textEdit.toPlainText()
        link = '{}/search?q={}&form=NPCTXT'.format(self.SEARCHURL, selected)
        QDesktopServices.openUrl(QUrl(link))

    def findedit(self):
        """查找"""
        print('查找')
        self.finderui.show()

    def findnext(self):
        """查找下一个"""
        print('查找下一个')
        self.finderui.findnext()

    def findlast(self):
        """查找上一个"""
        print('查找上一个')
        self.finderui.findlast()

    def repalceedit(self):
        """替换"""
        print('替换')
        self.replaceui.show()

    def replace_findnext(self, text, case, loop):
        """查找下一个"""
        self.findstr(text, case, loop, False)

    def replacestr(self, text1, text2, case, loop):
        """替换"""

        tc = self.textEdit.textCursor()
        selected = tc.selectedText()
        # 若当前选中等于查找内容则替换；否则先查找
        if selected and selected == text1:
            tc.removeSelectedText()
            tc.insertText(text2)
        else:
            self.findstr(text1, case, loop, False)

    def replaceall(self, text1, text2, case):
        """替换所有：使用正则直接替换"""
        content = self.textEdit.toPlainText()
        if not case:
            content = re.sub(text1, text2, content, flags=re.IGNORECASE)
        else:
            content = re.sub(text1, text2, content)
        self.textEdit.setText(content)

    def transto(self):
        """转到"""
        print('转到')
        self.transtoui.show()

    def get_transto_line(self, line):
        """获取目标行号"""
        print('转到%s行' % line)
        line = int(line)
        position = 0
        tc = self.textEdit.textCursor()
        # 获取目标行位置
        if line > 1:
            content = self.textEdit.toPlainText()
            while line > 1:
                try:
                    position_ = content.index('\n', position)
                    position = position_ + 1
                except:
                    break
                line -= 1
        tc.setPosition(position)
        self.textEdit.setTextCursor(tc)
        self.textEdit.setFocus()

    def selectall(self):
        """全选"""
        print('全选')
        self.textEdit.selectAll()

    def datetimeeidt(self):
        """时间/日期"""
        print('时间/日期')
        date = datetime.strftime(datetime.now(), "%H:%M %Y/%m/%d")
        self.textEdit.insertPlainText(date)

    def findstr(self, text, case, loop, backward):
        """查找"""
        print('查找')
        cursor = self.textEdit.textCursor()
        position = cursor.position()
        # # 根据方向及是否选中调整开始查找位置
        selected = cursor.selectedText()
        if backward:
            position -= len(selected)
        else:
            position += len(selected)
        tc = self.findstr_(position, text, case, backward)
        if tc.position() == -1:
            # 若选择了循环则更换起始位置重新查询
            if loop:
                if backward:
                    position = len(self.textEdit.toPlainText())
                else:
                    position = 0
                tc = self.findstr_(position, text, case, backward)
        if tc.position() == -1:
            return self.showmessage('找不到\n"{}"'.format(text))
        # 再次设置光标会自动选中查询结果
        self.textEdit.setTextCursor(tc)
        self.textEdit.setFocus()
        return tc

    def findstr_(self, position, text, case, backward=None):
        """查找"""
        # 若返回QCursor=-1则表示未找到
        doc = self.textEdit.document()
        options = ""
        if backward:
            options += "QTextDocument.FindBackward|"
        if case:
            options += "QTextDocument.FindCaseSensitively"
        else:
            options = options.rstrip('|')
        if options:
            tc = doc.find(text, position, eval(options))
        else:
            tc = doc.find(text, position)
        return tc

    # --------------------编辑菜单结束-----------------------------------------

    # --------------------格式菜单开始-----------------------------------------

    def auto_linefeed(self):
        """自动换行"""
        print('自动换行')
        if self.action_W.isChecked():
            self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        else:
            self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

    def set_font(self):
        """字体"""
        print('字体')
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setCurrentFont(font)

    def set_color(self):
        """增加了字体颜色设置"""
        print('字体颜色')
        col = QColorDialog.getColor()
        if col.isValid():
            self.textEdit.setTextColor(col)

    # --------------------格式菜单结束-----------------------------------------

    # --------------------查看菜单开始-----------------------------------------
    def enlarge(self):
        """缩放：放大"""
        print('放大')
        self.textEdit.zoomIn()
        self.zoomin += 1
        self.update_status_message()

    def narrow(self):
        """缩放：缩小"""
        print('缩小')
        self.textEdit.zoomOut()
        self.zoomin -= 1
        self.update_status_message()

    def restore_size(self):
        """缩放：恢复默认缩放"""
        print('恢复默认缩放')
        if self.zoomin:
            if self.zoomin > 0:
                self.textEdit.zoomOut(self.zoomin)
            else:
                self.textEdit.zoomIn(abs(self.zoomin))
            self.zoomin = 0
        self.update_status_message()

    def change_status(self):
        """状态栏"""
        print('状态栏')
        if self.action_S_2.isChecked():
            self.statusbar.show()
        else:
            self.statusbar.hide()

    # --------------------查看菜单结束-----------------------------------------
    # --------------------帮助菜单开始-----------------------------------------

    def gethelp(self):
        """查看帮助使用了百度搜索，支持下年老色衰的度娘"""
        print('查看帮助')
        link = 'https://www.baidu.com/s?wd={}'.format("获取有关+windows+10+中的记事本的帮助")
        QDesktopServices.openUrl(QUrl(link))

    def feedback(self):
        """查看帮助:没啥写的"""
        print('发送反馈')

    def about_notepad(self):
        """关于记事本"""
        print('关于记事本')
        self.aboutui.show()

    # --------------------帮助菜单结束-----------------------------------------
    # --------------------状态监听开始-----------------------------------------
    def textchanged(self):
        """若内容有变化则标识titel为*开头，表示未保存"""
        if not self.windowTitle().startswith('*'):
            self.update_windowtitle('*')

    def selectedchanged(self):
        """选中内容变化：更改复制、粘贴、删除的可用性"""
        if self.textEdit.textCursor().hasSelection():
            self.action_T_Ctrl_X.setEnabled(True)
            self.action_C_Ctrl_C.setEnabled(True)
            self.action_L_Del.setEnabled(True)
            self.action_rechoose.setEnabled(True)
        else:
            self.action_T_Ctrl_X.setEnabled(False)
            self.action_C_Ctrl_C.setEnabled(False)
            self.action_L_Del.setEnabled(False)
            self.action_rechoose.setEnabled(False)

    def positionchange(self):
        """鼠标位置变化：实时更新底部状态栏信息"""
        print('鼠标位置变化')
        self.update_status_message()

    def closeEvent(self, *args, **kwargs):
        """重新closeEvent方法，在窗体关闭前查看是否已保存"""
        print('关闭窗体')
        self.query_save()
    # --------------------状态监听结束-----------------------------------------
    # --------------------功能函数开始-----------------------------------------
    def init_statusbar(self):
        """初始化状态栏"""
        ql = QLabel(self)
        ql.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignHCenter)
        self.statusbar.addWidget(ql, 1)
        self.update_status_message()

    def update_status_message(self):
        """更新状态栏"""
        tc = self.textEdit.textCursor()
        row = tc.blockNumber() + 1
        col = tc.columnNumber() + 1
        zoom = format((10 + self.zoomin) / 10, ".0%")
        message = self.STATUS_MSG.format(row, col, zoom)
        self.statusbar.findChild(QLabel).setText(message)

    def isunsaved(self):
        """判断是否为未保存状态"""
        if self.windowTitle().startswith('*'):
            return True
        return False

    def update_windowtitle(self, prefix=''):
        """更新标题,提醒当前文档未保存"""
        if self.filename is None:
            filename = self.DEFAULTNAME
        else:
            filename = self.filename
        self.setWindowTitle("{}{} - {}".format(prefix, filename, self.DEFAULTSUFFIX))

    def showmessage(self, message):
        """消息展示"""
        messageBox = QMessageBox()
        messageBox.setWindowTitle(self.DEFAULTSUFFIX)
        messageBox.setText(message)
        messageBox.setStandardButtons(QMessageBox.Yes)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText('确定(Y)')
        messageBox.exec_()

    def addContextMenu(self):
        """自定义右键操作"""
        Menu = QMenu(self)
        Menu.addAction(self.action_U_Ctrl_Z)
        Menu.addSeparator()
        Menu.addAction(self.action_T_Ctrl_X)
        Menu.addAction(self.action_C_Ctrl_C)
        Menu.addAction(self.action_V_Ctrl_V)
        Menu.addAction(self.action_L_Del)
        Menu.addSeparator()
        Menu.addAction(self.action_A_Ctrl_A)
        Menu.addSeparator()
        action_l = QAction('从左到右的阅读顺序(R)', Menu)
        action_l.setCheckable(True)
        action_l.triggered.connect(lambda :self.deal_action_l(action_l))
        Menu.addAction(action_l)

        action_2 = QAction('显示 Unicode 控制字符(S)', Menu)
        action_2.setCheckable(True)
        action_2.triggered.connect(self.deal_action_2)
        Menu.addAction(action_2)

        Menu2 = QMenu("插入 Unicode 控制字符(I)",Menu)
        Menu.addMenu(Menu2)
        action_3 = QAction('Unicode 控制字符样例', Menu)
        action_3.triggered.connect(self.deal_action_3)
        Menu2.addAction(action_3)
        Menu.addSeparator()
        action_4 = QAction('打开输入法(O)', Menu)
        action_4.triggered.connect(self.deal_action_4)
        Menu.addAction(action_4)
        action_5 = QAction('汉字重选(R)', Menu)
        action_5.triggered.connect(self.deal_action_5)
        action_5.setEnabled(False)
        self.action_rechoose = action_5
        Menu.addAction(action_5)
        Menu.addSeparator()
        Menu.addAction(self.action_Bing_Ctrl_E)
        self.rightMenu = Menu

    def showContextMenu(self):
        """右键操作"""
        print('右键操作')
        self.rightMenu.exec_(self.cursor().pos())

    def deal_action_l(self,action):
        """设置从左到右阅读"""
        if action.isChecked():
            self.textEdit.setAlignment(QtCore.Qt.AlignRight)
        else:
            self.textEdit.setAlignment(QtCore.Qt.AlignLeft)

    def deal_action_2(self):
        """显示 Unicode 控制字符(S)"""
        print('显示 Unicode 控制字符(S)')
        pass
    def deal_action_3(self):
        """插入选中的 Unicode 控制字符"""
        print('插入选中的 Unicode 控制字符')
        pass
    def deal_action_4(self):
        """打开输入法(O)"""
        print('打开输入法(O)')
        pass
    def deal_action_5(self):
        """汉字重选(R)"""
        print('汉字重选(R)')
        tc = self.textEdit.textCursor()
        if tc.hasSelection():
            tc.setPosition(tc.position(),QTextCursor.MoveAnchor)
            self.textEdit.setTextCursor(tc)
    # --------------------功能函数结束-----------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = NotePad()
    win.show()
    sys.exit(app.exec_())
