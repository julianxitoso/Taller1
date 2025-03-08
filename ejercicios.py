# EJERCICIO 4

import random

def lista_aleatoria():
    numeros = [random.randint(1, 10) for _ in range(10)]
    for num in numeros:
        print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")
        

lista_aleatoria()

# EJERCICIO 3

frase = "El mejor regalo? El perdón..."
list_frase = list(frase)

list_frase = frase.split(" ")


list_frase.pop(3)
list_frase.pop(2)
list_frase.pop(0)
list_frase.insert(0,"el ")
list_frase.insert(2," ")

nueva_frase = ''.join(list_frase)
print(nueva_frase)