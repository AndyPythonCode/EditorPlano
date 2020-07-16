import sys #del sistema
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog #del sistema
from PyQt5.QtGui import QTextCursor #para mover el cursor hacia delante
from Editor import * #importamos nuesta ui
import txt as f #manejar de archivos
import appDirectorio as direct #app directorios, ventana

class AppEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directorio = direct.AppDirectorio()
        self.directorio.btnGuardar.clicked.connect(self.abrir)

        #Tamaño y fuente a nuestro textEdit
        self.text_usuario.setFont(QtGui.QFont("Times New Roman", self.spinBox.value()))
        #Metodos
        self.fontComboBox.currentFontChanged.connect(self.cambiar)
        self.spinBox.valueChanged.connect(self.tamano)
        self.actionOpen.triggered.connect(self.open)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardar_Como.triggered.connect(self.guardarComo)
        self.actionCreador.triggered.connect(self.creador)
        self.actionSalir.triggered.connect(self.salir)
        self.show()

    #funcion cursor en la ultima posicion
    def cursor(self):
        cursor = self.text_usuario.textCursor()
        cursor.movePosition(QTextCursor.End)
        return cursor

    def cambiar(self):
        #itemText(Necesita un indice) currentIndex(Me da ese indice) value(Me da el valor del spin)
        fuente = QtGui.QFont(self.fontComboBox.itemText(self.fontComboBox.currentIndex()), self.spinBox.value())
        self.text_usuario.setFont(fuente)

    #tamaño de letra con el spinBox
    def tamano(self):
        font = QtGui.QFont()
        font.setPointSize(self.spinBox.value())
        self.text_usuario.setFont(font)

    #informacion acerca de mi 
    def creador(self):
        f.mensaje('Creador','Nombre y correo electronico','Andy Arciniega andyarciniegas24@gmail.com',False)

    #abrirArchivo
    def open(self):
        self.directorio.configuracion()

    def abrir(self):
        if self.directorio.btnGuardar.text() == 'Abrir':
            txt = f.readFile(self.directorio.archivoTxt())
            self.text_usuario.setText(txt)
            self.directorio.hide()
        else:
            if len(self.directorio.getTextLine()) > 0:
                f.guardarComo(self.text_usuario.toPlainText(),self.directorio.getTextLine())
                self.directorio.hide()

    #guardar el archivo que hemos abrierto
    def guardar(self):
        valor = self.text_usuario.toPlainText()
        if len(valor) > 0:
            f.guardar(valor)
        else:
            f.mensaje("No Encontrado","Problema al guardar archivo no abrierto","Tienes que abrir un archivo primero",True)

    #guardar archivo abrierto con diferente nombre o el mismo
    def guardarComo(self):
        self.directorio.configuracionInicio()

    #cerrar la app
    def salir(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = AppEditor()
    sys.exit(app.exec_())