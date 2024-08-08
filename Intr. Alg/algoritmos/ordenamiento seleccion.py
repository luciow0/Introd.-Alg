def metodoseleccion(lista):
    largo = len(lista)
    for i in range (largo -1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux































