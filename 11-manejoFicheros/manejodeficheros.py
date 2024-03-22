import os
from os import path

class excepcionPropia(Exception):
    pass

class manejodeficheros:
    def crearFichero(self, name: str):
        try:
            if type(name) != str:
                raise excepcionPropia('El nombre del archivo deber ser del tipo string')
            file = open(name + '.txt', 'w')
            file.write('Hola mi user de github es ' + name + '\n')
            file.write('Mi edad es 25 años\n')
            file.write('Mi lenguaje de programacion favorito es Python, pero estoy aprendiendolo aun\n')
            file.close()
        except excepcionPropia as e:
            print(f"Error: {e}")

    def leerFichero(self):
        try:
            if not path.exists('espindola-lucas.txt'):
                raise excepcionPropia('No existe el archivo.')
            file = open('espindola-lucas.txt', 'r')
            for text in file.readlines():
                print(text)
            file.close()
        except excepcionPropia as e:
            print(f"Error: {e}")

    def borrarFichero(self):
        os.remove('espindola-lucas.txt')
        if not path.exists('espindola-lucas.txt'):
            print('El archivo se borro exitosamente')

nuevoFichero = manejodeficheros()
nuevoFichero.crearFichero('espindola-lucas')
nuevoFichero.leerFichero()
nuevoFichero.borrarFichero()