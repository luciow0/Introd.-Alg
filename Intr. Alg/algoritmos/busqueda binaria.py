def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista) -1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
        
    return pos

## necesario que la lista este ordenada