def metodo_burbuja(lista):
    desordenado = True
    
    while desordenado:
        desordenado = False

        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenado = True
