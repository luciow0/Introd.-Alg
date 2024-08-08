import random

def busquedaSecuencial(lista, dato):
    i = 0
    pos = -1
    print(i, lista[i],len(lista))
    while i < len(lista) and pos == -1:
        if lista[i] == dato:
            pos = i
        i += 1
        

    return pos


n = int(input("ingrese la cantidad de numeros que quiere ingresar a la lista"))
lista = []

aux = random.randint(0, 100) 
lista.append(aux)
print(lista[0])

for i in range(n -1): 
   
    aux = random.randint(0, 100)    
    ver = busquedaSecuencial(lista, aux)
    if ver == -1:
        lista.append(aux)      
        

print(lista)

##index error
