import random

def lista_aleatoria():
    numeros = [random.randint(1, 10) for _ in range(10)]
    for num in numeros:
        print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")
        

lista_aleatoria()