# ╔═════════════════════════════════════════════╗
# ║ Autor:  Lucas Espindola                     ║
# ║ GitHub: https://github.com/espindola-lucas  ║
# ║ 2024 -  Python                              ║
# ╚═════════════════════════════════════════════╝

# -----------------------------------
# * Principio S.O.L.I.D ISP
# -----------------------------------
# Mas info:

# 1. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones (interfaces o clases abstractas).
# 2. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

from abc import ABC, abstractmethod

# sin DIP

class Switch:

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self) -> None:
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


# lamp = Lamp()
# lamp.operate("on")
# lamp.operate("off")

# Con DIP

class AbstractSwitch:

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LampSwitch(AbstractSwitch):

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")