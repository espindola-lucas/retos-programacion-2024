class Animal: 
    def __init__(self, sonido, especie):
        self.sonido = sonido
        self.especie = especie

    def hacer_sonido(self):
        print(self.sonido)

    def describir(self):
        print(f"Soy un animal del tipo {self.especie} y mi sonido es un {self.sonido}")

class Perro(Animal):
    def __init__(self, sonido, especie):
        super().__init__(sonido, especie)

perro = Perro('Ladrido', 'Perro')
perro.describir()

class Gato(Animal):
    def __init__(self, sonido, especie):
        super().__init__(sonido, especie)

gato = Gato('Maullido', 'Gato')
gato.describir()