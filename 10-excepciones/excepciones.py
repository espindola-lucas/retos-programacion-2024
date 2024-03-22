class excepcionPropia(Exception):
    pass

class excepciones:
    def ejemploDeExcepciones(self):
        try:
            x = int(input("Ingrese un numero para el divisor: "))
            if x != 2:
                raise excepcionPropia("Solo se puede dividir por 2")
            resultado = 10/x
            print(f"10 divido por {x} es: {int(resultado)}")
        except ZeroDivisionError as e:
            print(f"No se puede dividir por 0: {e}")
        except ValueError as e:
            print(f"Solo se admiten numeros: {e}")
        except excepcionPropia as e:
            print(f"Error personalizado: {e}")

ej = excepciones()
ej.ejemploDeExcepciones()