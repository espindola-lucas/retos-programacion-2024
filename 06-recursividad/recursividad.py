def contador(n):
    if n >= 0:
        print(n)
        contador(n -1)
        
contador(100)

# Extra
# Calcular el factorial y el fibonacci usando recursividad.

def factorial(num: int) -> int:
    if num < 0:
        print("Los numeros negativos no tienen factorial")
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(f"Factorial de 5: {factorial(5)}")

def fibonacci(num: int) -> int:
    if num <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(f"Fibonacci de 5: {fibonacci(5)}")