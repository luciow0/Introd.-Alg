def busquedaSecuencial(lista, dato):
    i = 0
    pos = -1
    while pos == -1 and i <= len(lista):
        if lista[i] == dato:
                pos = i
        i += 1

    return pos