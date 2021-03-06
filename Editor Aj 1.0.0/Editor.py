# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'UI/Editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(638, 301)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(638, 301))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setProperty("value", 11)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.text_usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.text_usuario.setObjectName("text_usuario")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.text_usuario)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCreador = QtWidgets.QAction(MainWindow)
        self.actionCreador.setObjectName("actionCreador")
        self.menuArchivo.addAction(self.actionOpen)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionCreador)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text_usuario, self.fontComboBox)
        MainWindow.setTabOrder(self.fontComboBox, self.spinBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor Plano"))
        self.label.setText(_translate("MainWindow", "Letra:"))
        self.fontComboBox.setCurrentText(_translate("MainWindow", "Times New Roman"))
        self.label_2.setText(_translate("MainWindow", "Tamaño:"))
        self.text_usuario.setPlaceholderText(_translate("MainWindow", "Bienvenido!!! comienza a escribir"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Abrir"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como.."))
        self.actionGuardar_Como.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionCreador.setText(_translate("MainWindow", "Creador"))
