class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")

print("Prueba de clase")
instancia = Persona('Lucas', 25)
instancia.imprimir()

class Pila: 
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.is_empty():
            self.items.pop()
        else:
            print('La pila esta vacia')

    def imprimir(self):
        print(f"Datos de la pila: {self.items}")

print("Extras: ")
pila = Pila()
pila.apilar('Lucas')
pila.apilar('Rosario')
pila.apilar('Jorge')
pila.imprimir()
pila.desapilar()
print("Desapilamos la pila")
pila.imprimir()

class Cola: 
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def agregar(self, elemento):
        self.items.append(elemento)

    def eliminar(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            print('La pila esta vacia')

    def imprimir(self):
        print(f"Datos de la cola: {self.items}")

cola = Cola()
cola.agregar('Lucas')
cola.agregar('Rosario')
cola.agregar('Jorge')
cola.imprimir()
cola.eliminar()
print("Sacamos elemento de la cola")
cola.imprimir()