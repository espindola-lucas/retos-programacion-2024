# ╔═════════════════════════════════════════════╗
# ║ Autor:  Lucas Espindola                     ║
# ║ GitHub: https://github.com/espindola-lucas  ║
# ║ 2024 -  Python                              ║
# ╚═════════════════════════════════════════════╝

# -----------------------------------
# * Principio S.O.L.I.D ISP
# -----------------------------------
# Mas info:

# Es mejor tener muchas interfaces especificas y pequeñas que una interfaz grande,
# que obligue a los clientes a implementar metodos que no necesitan.

from abc import ABC, abstractmethod

# sin ISP

class WorkerInterface(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        # Los robots no comen
        pass


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()

# Con ISP

class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass


class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkInterface):

    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()