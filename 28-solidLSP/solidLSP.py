# ╔═════════════════════════════════════════════╗
# ║ Autor:  Lucas Espindola                     ║
# ║ GitHub: https://github.com/espindola-lucas  ║
# ║ 2024 -  Python                              ║
# ╚═════════════════════════════════════════════╝

# -----------------------------------
# * Principio S.O.L.I.D LSP
# -----------------------------------
# Mas info:

# Los objetos de una clase derivada deben poder ser reemplazados por objetos de la clase base,
# sin afectar el funcionamiento del sistema.
# Si una clase "S" es una subclase de una clase "T", entonces los objetos de tipo "T" deben poder
# ser sustituidos por objetos de tipo "S" sin alterar el comportamiento esperado del programa.

class Bird:
    def volar(self):
        raise NotImplementedError("Este metodo permite al ave volar")


class Duck(Bird):
    def volar(self):
        print("El pato sabe volar")


class Penguin(Bird):
    def volar(self):
        print("El pinguino no sabe volar")


def hacer_volar(ave: Bird):
    ave.volar()


pato = Duck()
pinguino = Penguin()
hacer_volar(pato)
hacer_volar(pinguino)