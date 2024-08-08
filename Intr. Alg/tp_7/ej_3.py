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

def VerSiEsCapicua(lis):
    capicua = True
    x = len(lis) // 2
    if lis[0] == lis[-1]:
        for i in range(1,x):
            if lis[i] == lis[-i -1]:
                capicua = True
            else:
                capicua = False
    else: 
        capicua = False

    return capicua

esOnoEs = VerSiEsCapicua(llamado)

if esOnoEs == True:
    print("es capicua") 

else:
    print("no es capicua")