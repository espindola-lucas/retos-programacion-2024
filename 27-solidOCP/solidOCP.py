# ╔═════════════════════════════════════════════╗
# ║ Autor:  Lucas Espindola                     ║
# ║ GitHub: https://github.com/espindola-lucas  ║
# ║ 2024 -  Python                              ║
# ╚═════════════════════════════════════════════╝

# -----------------------------------
# * Principio S.O.L.I.D OCP
# -----------------------------------
# Mas info: 

# El principio de abierto/cerrado (OCP, open-close principle) es otro de los pincipios S.O.L.I.D
# y establece de las entidades de software (clases, modulos, funciones, etc) deben estar abiertas
# para su extension, pero cerradas para su modificacion. En otras palabras, deberiamos poder extender
# el comportamiento de una clase sin modificar su codigo fuente.
# Aplicar el OCP en python implica diseñar el codigo de manera que podamos añadir nuevas funcionalidades
# sin alterar el codigo existente. Esto se puede lograr mediante la herencia, la composicion y el uso
# de interfaces o clases abstractas

# uso incorrecto OCP
# class AreaCalculator:
#     def calculate_area(self, shape):
#         if isinstance(shape, Circle):
#             return 3.14 * shape.radius * shape.radius
#         elif isinstance(shape, Rectangle):
#             return shape.width * shape.heigth

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

# class Rectangle:
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth

# en este ejemplo, si queremos añadir una nueva forma, como un triangulo, tendriamos que modificar
# la clase `AreaCalculator` lo cual viola el principio de OCP.

# uso correcto de OCP
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        
    def calculate_area(self):
        return self.width * self.heigth
    
class Triangle(Shape):
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth
    
    def calculate_area(self):
        return 0.5 * self.base * self.heigth
    
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

calculator = AreaCalculator()
print(calculator.calculate_area(circle))
print(calculator.calculate_area(rectangle))
print(calculator.calculate_area(triangle))

# 1. Hemos creado una clase abstracta Shape con un método abstracto calculate_area.
# 2. Las clases Circle, Rectangle y Triangle heredan de Shape y proporcionan su propia 
# implementación de calculate_area.
# 3. La clase AreaCalculator ahora depende de la abstracción Shape y puede calcular 
# el área de cualquier forma que implemente el método calculate_area

# De esta manera, si necesitamos añadir una nueva forma en el futuro, 
# simplemente creamos una nueva clase que herede de Shape y proporcione 
# su propia implementación de calculate_area, sin necesidad de modificar AreaCalculator. 
# Esto sigue el principio de abierto/cerrado (OCP), permitiendo la extensión del código 
# sin modificar el código existente.