from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from case import Ui_formAdd


class D_MainWindow(object):
    def __init__(self):
        super(D_MainWindow, self).__init__()
        #self.dialogs = list()

    def show_add_case_from(self):
        a = Ui_formAdd()
        self.dialog = QDialog()
        a.setupUi(self.dialog)
        #self.dialogs.append(a)
        self.dialog.show()
