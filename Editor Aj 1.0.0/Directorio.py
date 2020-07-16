# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Directorio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnGuardar = QtWidgets.QPushButton(Dialog)
        self.btnGuardar.setGeometry(QtCore.QRect(290, 280, 121, 31))
        self.btnGuardar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnGuardar.setObjectName("btnGuardar")
        self.textCrear = QtWidgets.QLineEdit(Dialog)
        self.textCrear.setGeometry(QtCore.QRect(20, 280, 261, 31))
        self.textCrear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textCrear.setObjectName("textCrear")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 401, 221))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 381, 191))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 91, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.listWidget, self.textCrear)
        Dialog.setTabOrder(self.textCrear, self.btnGuardar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Directorio"))
        self.label.setText(_translate("Dialog", "Archivos En mi Directorio"))
        self.btnGuardar.setToolTip(_translate("Dialog", "Guardar Directorio Default"))
        self.btnGuardar.setText(_translate("Dialog", "Guardar"))
        self.textCrear.setPlaceholderText(_translate("Dialog", "Para crear un archivo nuevo escriba aquí"))
        self.groupBox.setTitle(_translate("Dialog", "Seleccione uno"))
        self.label_3.setText(_translate("Dialog", "Crear Nuevo:"))
