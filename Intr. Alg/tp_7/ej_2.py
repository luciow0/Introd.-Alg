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

def sumadorlista(lis):
    suma = 0
    x = len(lis)
    for i in range(x):
        suma += lis[i]
    return suma

llamolasuma = sumadorlista(llamado)

print("el resultado de la suma de las listas es ", llamolasuma)