import random 
lista = []

n = int(input("Ingrese la cantidad de elementos que contendra la lista"))

for i in range(0, n-1):
    lista.append(random.randint(1, 20))
    if lista