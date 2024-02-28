
# pila

pila = []

def apilar(num: int):
    pila.append(num)

def desapilar():
    pila.pop()

apilar(1)
apilar(4)
apilar(9)
print(f"Datos de la pila: {pila}")

desapilar()
print(f"Desapilamos la pila: {pila}")

# cola
cola = []

def agregar(elemento):
    cola.append(elemento)


def quitar():
    return cola.pop(0)

agregar(1)
agregar(2)
agregar(3)
print(f"Datos de la cola: {cola}")

print(quitar())
print(f"Sacamos un elemento de la cola: {cola}")