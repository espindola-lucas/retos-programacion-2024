class Decorator:
    def my_decorator(self, func):
        def funcion_(a, b):
            print('Antes de llamar a la funcion')
            resultado = func(a, b)
            print('Se llamo ala funcion')
            return resultado
        return funcion_
    
    def sum(self, a, b):
        print('entro a la funcion suma')
        return a+b

# decorador = Decorator()
# decorador.sum = decorador.my_decorator(decorador.sum)
# sum_dec = decorador.sum(4, 5)
# print(sum_dec)

# extra
class Decorator_count:
    def count_call(self, func):
        def new_fun():
            new_fun.contador += 1
            print(f"La funcion {func.__name__} ha sido llamada {new_fun.contador} veces")
            return func
        new_fun.contador = 0
        return new_fun
    
    def my_func(self):
        print('ejecuntado la funcion')

decorador = Decorator_count()
decorador.my_func = decorador.count_call(decorador.my_func)

print(decorador.my_func())
print(decorador.my_func())
print(decorador.my_func())