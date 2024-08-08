import random
"""Leer dos listas de M y N numeros y ordenarlas de menor a mayor
    Luego se solicita generar e imprimir una tercera lista que resulte de intercalar los elementos de M Y n
    La nueva lista tambien debe quedar ordenada, sin utilizar ningun metodo de ordenamiento en ella"""


def ordenamiento(lista_A):
    n = len(lista_A)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_A[j] > lista_A[j+1]:
                lista_A[j], lista_A[j+1] = lista_A[j+1], lista_A[j]
    return lista_A

def generados_listas():
    lista_1 = []
    lista_2 = []
    N = int(input("ingrese la cantidad de numeros que desea agregar a la lista 1 "))
    M = int(input("ingrese la cantidad de elementos que desea agregar a la lista 2 "))

    return cargar_listas(lista_1,lista_2, N, M)

def cargar_listas(lista_1,lista_2, N, M):
    for i in range(0,N):
        aux = random.randint(0, 100)
        lista_1.append(aux)
    for j in range(0,M):
        axu = random.randint(0,100)
        lista_2.append(axu)

    print("lista desordenada 1 ", lista_1,"\n","lista desordenda 2", lista_2)

    return ordenar_listas(lista_1, lista_2)    

def ordenar_listas(lista_1,lista_2):
    ordenar_1 = ordenamiento(lista_1)
    ordenar_2 = ordenamiento(lista_2)
    print("lista ordenada 1 ")
    print(ordenar_1)
    print("lista ordenada 2 ")
    print(ordenar_2)


generados_listas()