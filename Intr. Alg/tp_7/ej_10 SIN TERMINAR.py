import random

lista1= []
lista2= []

def busquedaSec(lista,obj):
    pos = -1
    i = 0
    while pos == -1 and i <= len(lista):
        if lista[i] == obj:
            pos = i
        
        i += 1

    return pos

  
def eliminador(listaoriginal,listaborrar):
    n = len(listaoriginal)
    for i in range(n-1):
        obj = listaborrar[i]
        remove = busquedaSec(listaoriginal, obj)
        if remove != -1:
            del listaoriginal[obj]
    
    return listaoriginal



for i in range (100):
    aux = random.randint(0, 100)
    lista1.append(aux)

for i in range (100):
    aux = random.randint(0, 100)
    lista2.append(aux)

n = len(lista1)

for i in range(n -1):
    repetidos = []
    if lista1[i] == lista2[i]:
        repetidos.append(lista1[i])
  

llamada = eliminador(lista1, lista2)

print(lista1)
print(lista2)
print(llamada)