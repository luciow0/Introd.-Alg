def cargardatos(A , B):
    lista = []

    if A < B:

        print("ingrese su valor entre " , A , "y ", B)
        n = float(input(" "))

        while n != -1:

            if (n < A or n > B):
                print("numero invalido, ingrese un valor correcto")
                n = float(input("ingrese su valor valido"))
    
            else:
                lista.append(n)
                n = float(input("ingrese su siguiente valor, -1 para finalizar "))
        
    else:
        
        print("ingrese su valor entre " , B , "y ", A)
        n = float(input(" "))

        while n != -1:

            if (n < B or n > A):
                print("numero invalido, ingrese un valor correcto")
                n = float(input("ingrese su valor valido"))
    
            else:
                lista.append(n)
                n = float(input("ingrese su siguiente valor, -1 para finalizar "))

    return lista 

def insercion(lista):
    for i in range(1, len(lista)):
        aux = lista [i]
        j = i
        while j > 0 and (lista[j-1] > aux):
            lista[j] = lista[j-1]
            j = j -1
            lista[j] = aux
    return lista


def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista) -1
    listaBuscado = []
    while izq <= der:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            listaBuscado.append(centro)
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    
    return listaBuscado


minimo = float(input("ingrese un valor minimo para la lista"))
maximo = float(input("ingrese un valor maximo para la lista"))

llamado = cargardatos(minimo, maximo)

print(llamado)

aVerSianda = insercion(llamado)

print(aVerSianda)

valor = int(input("Ingrese el valor que desea bucar"))

invocar = busquedaBinaria(aVerSianda, valor)

print("el valor buscado", valor, "esta en las posiciones", invocar)
