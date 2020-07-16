from Directorio import *
from PyQt5.QtWidgets import QDialog
import txt as f

class AppDirectorio(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.itemClicked.connect(self.archivoTxt)

    def configuracion(self):
        self.verDirectorios()
        self.listWidget.clear()
        self.btnGuardar.setText("Abrir")
        self.textCrear.setReadOnly(True)
        self.textCrear.setPlaceholderText("No esta disponible esta opcion")
        for i in f.directorio():
            self.listWidget.addItem(i)

    def configuracionInicio(self):
        self.verDirectorios()
        self.listWidget.clear()
        self.btnGuardar.setText("Guardar")
        self.textCrear.setReadOnly(False)
        self.textCrear.setPlaceholderText("Escriba Aca")
        for i in f.directorio():
            self.listWidget.addItem(i)

    def archivoTxt(self):
        for i in self.listWidget.selectedItems():
            return i.text()

    def getTextLine(self):
        return self.textCrear.text()

    def verDirectorios(self):
        self.show()