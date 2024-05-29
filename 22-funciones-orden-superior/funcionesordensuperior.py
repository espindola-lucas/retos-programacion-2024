from statistics import mean
from datetime import datetime
import json

class FunctionalExamples:
    def __init__(self):
        pass

    # Ejemplo de map que aplica una funcion a cada elemento de una lista
    def square(self, x):
        return x * x

    def get_square_numbers(self, numbers):
        return list(map(self.square, numbers))

    # Ejemplo funcion que devuelve otra funcion
    def make_adder(self, n):
        def adder(x):
            return x + n
        return adder

    # Ejemplo de funcion que recibe y devuelve una funcion
    def apply_twice(self, func, arg):
        return func(func(arg))

    def add_one(self, x):
        return x + 1

    # Ejemplo usando lambda
    def get_square_numbers_with_lambda(self, numbers_list):
        return list(map(lambda x: x * x, numbers_list))

if __name__ == "__main__":
    fe = FunctionalExamples()

    # Ejemplo de map que aplica una funcion a cada elemento de una lista
    numbers = [1, 2, 3, 4, 5]
    square_numbers = fe.get_square_numbers(numbers)
    # print("Cuadrado de numeros usando map:", square_numbers)

    # Ejemplo funcion que devuelve otra funcion
    add_5 = fe.make_adder(5)
    # print("Suma 5 a 10 usando make_adder::", add_5(10))

    # Ejemplo de funcion que recibe y devuelve una funcion
    # print("Aplicar add_one dos veces a 5:", fe.apply_twice(fe.add_one, 5))

    # Ejemplo usando lambda
    numbers_list = [1, 2, 3, 4, 5]
    square_numbers_list = fe.get_square_numbers_with_lambda(numbers_list)
    # print("Números cuadrados usando lambda:", square_numbers_list)
    
# extra
class Students:
    STUDENTS = [
        {"name": "Alice", "dob": "2001-05-15", "grades": [8.5, 9.0, 9.5]},
        {"name": "Bob", "dob": "2000-08-22", "grades": [7.0, 6.5, 8.0]},
        {"name": "Charlie", "dob": "2002-01-10", "grades": [9.0, 9.5, 10.0]},
        {"name": "David", "dob": "2001-12-02", "grades": [6.0, 7.5, 7.0]}
    ]
    
    def average_grades(self) -> list:
        """
            Obtiene una lista de estudiantes por nombre
            y promedio de sus calificaciones
        """
        names_average = map(lambda student: {
            "name": student['name'], 
            "average": sum(student["grades"]) / len(student["grades"])
            }, Students.STUDENTS)
        return list(names_average)

    def best_students(self, umbral) -> list:
        """
            Obtiene una lista con el nombre de los estudiantes
            que tienen calificaciones con un 9 o más de promedio
        """
        high_avg_students = filter(
            lambda student: sum(student["grades"]) / len(student["grades"]) >= umbral, students.STUDENTS 
        )
        names = map(lambda student: student["name"], high_avg_students)
        return list(names)

    def birth(self) -> list:
        """
        Obtiene una lista de estudiantes ordenada desde el más joven.
        """
        young_students = sorted(
            Students.STUDENTS,
            key=lambda student: datetime.strptime(student["dob"], "%Y-%m-%d"),
            reverse=True
        )
        
        get_names_birth = list(map(lambda student: {"name": student["name"], "dob": student["dob"]}, young_students))
        
        return (get_names_birth)
        
    def high_grade(self) -> float:
        """
        Obtiene la calificación más alta de entre todas las de los alumnos.
        Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
        """
        all_grades = [grade for student in Students.STUDENTS for grade in student["grades"]]
        valid_grades = [grade for grade in all_grades if 0 <= grade <= 10]
        if valid_grades:
            max_grade = max(valid_grades)
            return max_grade
        else:
            return None

students = Students()

# print(json.dumps(students.average_grades(), indent=4))

# print(json.dumps(students.best_students(9.0), indent=4))

# print(json.dumps(students.birth(), indent=4))

print(students.high_grade())

