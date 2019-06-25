from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from case import Ui_formAdd


class D_MainWindow(object):
    def __init__(self):
        super(D_MainWindow, self).__init__()
        self.dialog = QDialog()

    def show_add_case_from(self):
        a = Ui_formAdd()
        # set up ui 是qtdesginer工具生成的函数，可以把生成的窗体信息设置到一个dialog或者window中去
        # 需要注意的是生成出来的class无法直接show，此外容器还必须放入主线程类的对象中，否则会一闪而过（由于show完之后立马继续运行，与win平台的差异不会默认在主线程中show）
        a.setupUi(self.dialog)
        self.dialog.show()
