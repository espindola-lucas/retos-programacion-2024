import time
import random

"""
Un callback es una función que se pasa como argumento a otra función y se ejecuta después
de que se completa la operación de esa función. Los callbacks se utilizan frecuentemente
en programación asíncrona, como en JavaScript, para manejar eventos o realizar tareas 
después de que una operación se haya completado, como una solicitud HTTP o una operación de 
lectura/escritura en un archivo.
"""

class Callbacks:
    """
    1. Se utiliza `fetch_data` para simular una operación asíncrona y se pasa handle_data como callback.
    2. `handle_data` se ejecuta después de que fetch_data ha completado su `operacion`.
    """
    
    def fetch_data(self, callback):
        print("Fetching data...")
        time.sleep(2)
        data = {"name": "Lucas", "age": 25}
        callback(data)
        
    def handle_data(self, data):
        print("Data received:", data)

# call = Callbacks()
# call.fetch_data(call.handle_data)

# extra challenge

class CallbackOrder:
    """
    Crear un simulador de pedidos utilizando callback. 
    Debe aceptar el nombre del plato, un callback de confirmacion, una de listo
    y otra de entrega.
    - Debe imprimir un confirmacion cuando empiece el procesamiento.
    - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
    - Debe invocar a cada callback siguiendo un orden de procesado.
    - Debe notificar que el plato esta listo o ha sido entregado.
    """

    def __init__(self, dish_name):
        self._dish_name = dish_name

    def get_name_dish(self):
        return self._dish_name
        
    def prepare_dish(self, callback):
        print("Procesando...")
        time.sleep(2)
        print(f"Preparando el plato: {self.get_name_dish()}")  
        time.sleep(random.randrange(1, 10))      
        callback()

    def ready_dish(self, callback):
        print("Plato listo para entregar")
        time.sleep(random.randrange(1, 10))
        callback()
        
    def delivered_dish(self):
        print("Plato entregado")

handler = CallbackOrder(str(input('Ingrese un nombre de plato: ')))
handler.prepare_dish(lambda: handler.ready_dish(handler.delivered_dish))