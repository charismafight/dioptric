# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formAdd(object):
    def setupUi(self, formAdd):
        formAdd.setObjectName("formAdd")
        formAdd.resize(380, 157)
        formAdd.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(formAdd)
        self.buttonBox.setGeometry(QtCore.QRect(10, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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
        self.txtName = QtWidgets.QLineEdit(formAdd)
        self.txtName.setGeometry(QtCore.QRect(50, 10, 81, 20))
        self.txtName.setObjectName("txtName")
        self.txtAge = QtWidgets.QLineEdit(formAdd)
        self.txtAge.setGeometry(QtCore.QRect(50, 40, 61, 20))
        self.txtAge.setObjectName("txtAge")
        self.txtEyesight = QtWidgets.QLineEdit(formAdd)
        self.txtEyesight.setGeometry(QtCore.QRect(50, 70, 61, 20))
        self.txtEyesight.setObjectName("txtEyesight")
        self.txtIdentity = QtWidgets.QLineEdit(formAdd)
        self.txtIdentity.setGeometry(QtCore.QRect(250, 40, 121, 20))
        self.txtIdentity.setText("")
        self.txtIdentity.setObjectName("txtIdentity")
        self.cbSex = QtWidgets.QComboBox(formAdd)
        self.cbSex.setGeometry(QtCore.QRect(250, 10, 51, 22))
        self.cbSex.setObjectName("cbSex")
        self.cbSex.addItem("")
        self.cbSex.addItem("")
        self.label_5 = QtWidgets.QLabel(formAdd)
        self.label_5.setGeometry(QtCore.QRect(120, 40, 16, 21))
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
        self.cbSex.setItemText(0, _translate("formAdd", "男"))
        self.cbSex.setItemText(1, _translate("formAdd", "女"))
        self.label_5.setText(_translate("formAdd", "岁"))

