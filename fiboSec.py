#Jhonier Mendez Bravo - 2372226
#David Santiago Guerrero Delgado - 2324594
#Cristian Daniel Guaza Mejia - 2372225

from time import time

secuencia = []

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n - 1) + fibo(n - 2)

def main():
  ti = time()

  for i in range(1, 145, 1):
    secuencia.append(33)

  for i in range(0, 144, 1):
    secuencia[i] = fibo(secuencia[i])

  print(f"Se tardó: {time() - ti}")

if _name_ == "_main_":
  main()