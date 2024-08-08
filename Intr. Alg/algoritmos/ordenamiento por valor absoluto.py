def obtenercalve(elemento):
    rta = elemento 
    if elemento<0:
        rta -elemento
    return rta


def metodoseleccion(lista):
    largo = len(lista)
    for i in range (largo-1):
        for j in range(i+1, largo):
            if obtenercalve(lista[i])>obtenercalve(lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    return lista