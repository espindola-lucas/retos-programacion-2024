import logging
import random
import sys

class Logs:
    def defferentsLogs(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%Y-%b-%d %H:%M:%S')
        
        logging.debug('Test see debug')
        logging.info('Test see info')
        logging.warning('Test see warning')
        logging.error('Test see error')
        logging.critical('Test see critical')
        
logs = Logs()
# logs.defferentsLogs()

class TaskManager:
    def __init__(self):
        self.tasks = {}
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%Y-%b-%d %H:%M:%S')
        logging.info('Gestor de tareas inicializado')
        
    def addTasK(self):
        name = input('Ingrese el nombre de la tarea: ')
        description = input('Ingrese la descripcion de la tarea: ')
        if name in self.tasks:
            logging.warning(f"Intento agregar una tarea ya existente: {name}")
            return
        execution_time = random.randint(1, 5)
        self.tasks[name] = {
            "description": description,
            "execution_time": execution_time
        }
        logging.info(f"Tarea {name} agregada")
        logging.debug(f"TIempo de ejecucion de la tarea: {name}: {execution_time} segundos")

    def delete_task(self):
        name = input('Ingrese el nombre de la tarea a eliminar: ')
        if name not in self.tasks:
            logging.warning(f"Intento de eliminar una tarea que no existe: {name}")
            return
        del self.tasks[name]
        logging.info(f"Tarea {name} eliminada")

    def list_task(self):
        if not self.tasks:
            logging.info("No hay tareas para listar")
            return
        for name, info in self.tasks.items():
            print(f"Tarea: {name} - Descripcion: {info['description']} - Tiempo de ejecucion: {info['execution_time']} segundos")
            logging.info(f"Tiempo de ejecucion de la tarea {name} es {info['execution_time']} segundos")

manager = TaskManager()

while True:
    print("\nGestor de Tareas")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Listar tareas")
    print("4. Salir")

    choice = input('Seleccione una opcion: ')
    match choice:
        case '1':
            manager.addTasK()
        case '2':
            manager.delete_task()
        case '3':
            manager.list_task()
        case '4':
            sys.exit(0)
        case _:
            print('opcion no valida, por favor intente de nuevo')