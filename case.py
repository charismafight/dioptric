# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formAdd(QtGui.QWindow):
    def setupUi(self, formAdd):
        formAdd.setObjectName("formAdd")
        formAdd.resize(400, 187)
        formAdd.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(formAdd)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblName = QtWidgets.QLabel(formAdd)
        self.lblName.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.lblName.setObjectName("lblName")
        self.label = QtWidgets.QLabel(formAdd)
        self.label.setGeometry(QtCore.QRect(190, 10, 54, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(formAdd)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(formAdd)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 54, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(formAdd)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 54, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(formAdd)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(formAdd)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 40, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(formAdd)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 70, 51, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(formAdd)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 40, 141, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(formAdd)
        self.comboBox.setGeometry(QtCore.QRect(250, 10, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(formAdd)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 16, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(formAdd)
        self.buttonBox.accepted.connect(formAdd.accept)
        self.buttonBox.rejected.connect(formAdd.reject)
        QtCore.QMetaObject.connectSlotsByName(formAdd)

    def retranslateUi(self, formAdd):
        _translate = QtCore.QCoreApplication.translate
        formAdd.setWindowTitle(_translate("formAdd", "患者信息"))
        self.lblName.setText(_translate("formAdd", "姓名："))
        self.label.setText(_translate("formAdd", "性别："))
        self.label_2.setText(_translate("formAdd", "年龄："))
        self.label_3.setText(_translate("formAdd", "身份证号："))
        self.label_4.setText(_translate("formAdd", "视力："))
        self.label_5.setText(_translate("formAdd", "岁"))
