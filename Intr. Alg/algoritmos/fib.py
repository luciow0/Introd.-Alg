a1 = 0
a2= 1
acumulador = 0
n = int(input("ingrese "))

for i in range(n):

    a = a1 + a2
    a2 = a
    a1 = a2 - a1
    acumulador += a
    print("el termino a es ", a)