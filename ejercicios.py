# EJERCICIO 4

import random
# Ejercicio 1
def abecedario(n):
  abeced = 'abcdefghijklmnopqrstuvwxyz'
  listabc = list(abeced)
  for i in range(27):
    if (i % n != 0):
      print(listabc[i-1])

abecedario(3)

# Ejercicio 2
def vocales(frase):
  vowels = ['a', 'e', 'i', 'o', 'u']
  numvowels =[0,0,0,0,0]
  cuentavocal = 0
  for i in range(5):
    numvowels[i] = frase.count(vowels[i])
    #print('La frase tiene',numvowels[i],"veces la vocal '",vowels[i],"'.")
    cuentavocal = cuentavocal + numvowels[i]
  print(cuentavocal)

vocales("otorrinoralingologo")

import random
def lista_aleatoria():
    numeros = [random.randint(1, 10) for _ in range(10)]
    for num in numeros:
        print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")
        

lista_aleatoria()

# EJERCICIO 3.

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

