def busqueda_sec(obj,lista):
    i = 0
    pos = -1
    n = len(lista)
    while pos == -1 and i < n : 
        if lista[i] == obj: 
            pos = i
        i = i + 1  
    return pos
def burbuja(lista):
    desordenado = True
    while desordenado: 
        desordenado = False
        for i in range(len(lista) - 1): 
            if lista[i] < lista[i + 1]: 
                aux = lista[i+ 1]
                lista[i + 1] = lista[i]
                lista[i] = aux
                desordenado = True
    return lista

unidad = []
metros = []
precios = []
n = int(input("ingrese el numero de unidad "))
j = 0

while j<= 2:
    
    ver = busqueda_sec(n, unidad)
    if ver == -1:
        unidad.append(n)
        m = int(input("ingrese los metros de su unidad "))
        metros.append(m)
        precio = int(input("ingrese el precio x metro cuadrado"))
        precios.append(precio)
        n = int(input("ingrese el numero de unidad "))

    else: 
        n = int(input("ingrese el numero de unidad no repetido "))

    j += 1

print(unidad, metros, precios)
promedio = 0

for i in range(len(unidad)): 
    promedio += metros[i] * precios[i]

promedio = promedio / len(unidad)
print(promedio)