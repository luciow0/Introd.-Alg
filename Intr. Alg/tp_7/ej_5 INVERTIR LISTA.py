def cargardatos(A , B):
    lista = []

    if A < B:
        print("ingrese su valor entre " , A , "y ", B)
        n = int(input(" "))
        while n != -1:
            if (n < A or n > B):
                print("numero invalido, ingrese un valor correcto")
                n = int(input("ingrese su valor valido"))
            else:
                lista.append(n)
                n = int(input("ingrese su siguiente valor, -1 para finalizar "))
    else:
        print("ingrese su valor entre " , B , "y ", A)
        n = int(input(" "))
        while n != -1:
            if (n < B or n > A):
                print("numero invalido, ingrese un valor correcto")
                n = int(input("ingrese su valor valido"))
            else:
                lista.append(n)
                n = int(input("ingrese su siguiente valor, -1 para finalizar "))
    return lista 

minimo = int(input("ingrese un valor minimo para la lista"))
maximo = int(input("ingrese un valor maximo para la lista"))

llamado = cargardatos(minimo, maximo)
print(llamado)

def invertirLista(lis):
    n = len(lis)
    for i in range(n // 2):
        aux = lis[i]
        lis[i] = lis[n - i - 1]
        lis[n - i - 1] = aux

    return lis

verSiAnda = invertirLista(llamado)
print(verSiAnda)