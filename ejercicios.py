import random

def lista_aleatoria():
    numeros = [random.randint(1, 10) for _ in range(10)]
    for num in numeros:
        print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")
        

lista_aleatoria()


def abecedario(n):
  abeced = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
  listabc = abeced.split(',')
  for i in range(27):
    if (i % n != 0):
      print(listabc[i-1])


def vocales(frase):
  vowels = ['a', 'e', 'i', 'o', 'u']
  numvowels =[0,0,0,0,0]
  cuentavocal = 0
  for i in range(5):
    numvowels[i] = frase.count(vowels[i])
    #print('La frase tiene',numvowels[i],"veces la vocal '",vowels[i],"'.")
    cuentavocal = cuentavocal + numvowels[i]
  print(cuentavocal)