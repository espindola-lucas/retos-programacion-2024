import os
import json
import xml.etree.ElementTree as ET
from os import path

class excepcionPropia(Exception):
    pass

class managerFicheros:
    def __init__(self, path: str, nameFile: str, name: str):
        self.path = path
        self.nameFile = nameFile
        self.name = name
    
    def llenarFichero(self):
        try:
            if type(self.nameFile) != str:
                raise excepcionPropia('El nombre del archivo deber ser del tipo string')
            if self.nameFile[-3:] == 'xml':
                crearXML = jsonYxml(self.path, self.nameFile, self.name)
                crearXML.crearArchivoXML('xml')
            else:
                crearJSON = jsonYxml(self.path, self.nameFile, self.name)
                crearJSON.crearArchivoXML('json')
        except excepcionPropia as e:
            print(f"Error: {e}")

    def leerFichero(self):
        try:
            if not path.exists(os.getcwd() + self.path + self.nameFile):
                raise excepcionPropia('No existe el archivo.')
            file = open(os.getcwd() + self.path + self.nameFile, 'r')
            for text in file.readlines():
                print(text)
            file.close()
        except excepcionPropia as e:
            print(f"Error: {e}")

    def borrarFichero(self):
        os.remove(os.getcwd() + self.path + self.nameFile)
        if not path.exists(os.getcwd() + self.path + self.nameFile):
            print('El archivo se borro exitosamente')

class jsonYxml(managerFicheros):

    def __init__(self, path: str, nameFile: str, name: str):
        super().__init__(path, nameFile, name)

    def crearArchivoXML(self, type: str):
        # el modulo es necesario que sea importado explicitamente en el alcance local para ser utilizado
        import xml.dom.minidom

        data = {'name': self.name, 'edad': 'Mi edad es 25 años', 'fec_nacimiento': '13/10/1998', 'languages': 'PHP - Python - JavaScript - Bash - C#'}
        if type == 'xml':
            xml_data = ET.Element('data')
            for key, value in data.items():
                element = ET.SubElement(xml_data, key)
                element.text = value
            
            xml_str = xml.dom.minidom.parseString(ET.tostring(xml_data)).toprettyxml(indent='    ')
            file_path = os.path.join(os.getcwd() + self.path + self.nameFile)
        
            with open(file_path, 'w') as f:
                f.write(xml_str)
        else:
            file_path = os.path.join(os.getcwd() + self.path + self.nameFile)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

print('Ejemplo XML: \n')
xml = jsonYxml('/12-JSONyXML/', 'ejemplo.xml', 'Lucas')
xml.llenarFichero()
xml.leerFichero()
xml.borrarFichero()

print('Ejemplo JSON: \n')
jsonFile = jsonYxml('/12-JSONyXML/', 'ejemplo.json', 'Lucas')
jsonFile.llenarFichero()
jsonFile.leerFichero()
jsonFile.borrarFichero()