import os
from PyQt5.QtWidgets import QMessageBox

__openFile = ''

def mensaje(titulo, text, informativo, bandera):
    mensaje = QMessageBox()
    if bandera:
        mensaje.setIcon(QMessageBox.Critical)
    mensaje.setWindowTitle(titulo)
    mensaje.setText(text)
    mensaje.setInformativeText(informativo)
    mensaje.setStandardButtons(QMessageBox.Ok)
    mensaje.exec_()
    
def readFile(nombre):
    f = open(f'Notas/{nombre}', 'r')
    global __openFile 
    __openFile = nombre
    return f.read()

def guardar(textoBox):
    w = open(f"Notas/{__openFile}", "w")
    w.write(textoBox)
    w.close()

def guardarComo(textoBox, nombre):
    w = open(f"Notas/{nombre}.txt", 'w')
    w.write(textoBox)
    w.close()
    
def directorio():
    return os.listdir('Notas')