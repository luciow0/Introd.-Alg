def metodoinsercion(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i
        while j>0 and lista[j-1]>aux:
            lista[j] = lista[j-1]
            j = j - 1 
            lista[j] = aux