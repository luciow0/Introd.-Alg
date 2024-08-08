def leervendedor(maximo):
    n = int(input("Numero de vendedor (-1 para terminar) "))
    while n!=-1 and (n<1 or n>maximo):
        print("*** Vendedor invalido ***")
        n = int(input("Numero de vendedor (-1 para terminar ) "))
        return n

#programa principal 
vendedores = 50

#creamos la lista y la inicializamos en 0 
ventas = []
for i in range(vendedores+1):
    ventas.append(0)

#comenzamos la lectura y acumulacion de datos
vendedor = leervendedor(vendedores)
while vendedor !=-1:
    importe = int(input("importe de la venta? "))
    ventas[vendedor] = ventas[vendedor]+importe
    vendedor = leervendedor(vendedores)

#imprimir informe final 
for i in range(1, vendedores):
    print("el vendedor",i,"vendio $ ", ventas[i])
