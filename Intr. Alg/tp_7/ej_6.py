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


minimo = float(input("ingrese un valor minimo para la lista"))
maximo = float(input("ingrese un valor maximo para la lista"))

llamado = cargardatos(minimo, maximo)

print(llamado)


def listaPosi(lis,valorBuscado):
    n = len(lis)
    pos = 0
    lista_posiciones = []
    for i in range(n - 1 ):
        pos = i
        if lis[i] == valorBuscado:
            lista_posiciones.append(pos)

    return lista_posiciones


valor = int(input("ingrese el valor que desea ubicar en la lista "))

verSiaNda = listaPosi(llamado, valor)

print("el valor buscado ", valor, "fue encontrado en las posiciones ", verSiaNda)
