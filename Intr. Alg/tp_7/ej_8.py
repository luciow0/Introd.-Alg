import random
lista = []
auxiliar = random.randint(0, 100)

while auxiliar != 0:
    lista.append(auxiliar)
    auxiliar = random.randint(0,100)

print(lista)

n = len(lista)
for i in range(n - 1):
    if i == 0:
        valor_minimo = lista[i]
        lugar_que_ocupa = i

    elif lista[i] < valor_minimo:
        valor_minimo = lista[i]
        lugar_que_ocupa = i

def busquedaSec(lista,obj):
    n = len(lista)
    repetidos = 0
    listaBuscado = []
    for i in range(n - 1):
        if lista[i] == obj:
            listaBuscado.append(i)
            repetidos += 1
    return listaBuscado, repetidos


print("valor minimo de la lista ", valor_minimo)



variosRep, lool = busquedaSec(lista, valor_minimo)

if lool > 1 :
    print("valor encontrado en los lugares ", variosRep) 

else:
    print("lugar que ocupa ", lugar_que_ocupa)

   







