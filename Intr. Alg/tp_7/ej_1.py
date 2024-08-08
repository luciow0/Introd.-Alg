def cargardatos(A , B):
    lista = []
    if A <= B:
        minimo = A
        maximo = B
    else:
        minimo = B
        maximo = A 
    print("ingrese su valor entre " , A , "y ", B)
    n = int(input(" "))
    while n != -1: 
        if (n < minimo or n > maximo):
            print("numero invalido, tiene que estar dentro del rango")
        else:
            lista.append(n) 
        n = int(input("ingrese su siguiente valor, -1 para finalizar ")) 
    return lista 

minimo = int(input("ingrese un valor minimo para la lista"))
maximo = int(input("ingrese un valor maximo para la lista"))

llamado = cargardatos(minimo, maximo)
print(llamado)




