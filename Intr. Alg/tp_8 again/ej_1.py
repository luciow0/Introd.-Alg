def ordenar_burbuja(lista, lista_2):
    desordenado = True
    while desordenado:
        desordenado = False 
        for i in range(len(lista) - 1): 
            if lista[i] < lista[i + 1]:
                aux = lista[i + 1]
                lista[i+1] = lista[i]
                lista[i] = aux
                aux = lista_2[i + 1]
                lista_2[i + 1] = lista_2[i]
                lista_2[i] = aux
                desordenado = True
    return(lista_2,lista)
    

legajo = int(input("Ingrese legajo "))
legajos = []
notas = []
apronados = 0
desaprobados = 0 
cant_alumnos = 0
notas_total = 0
matriz = [[],[]]

while legajo != -1:
    nota = int(input("Ingrese nota "))
    while nota < 1 or nota > 10:
        nota = int(input("Ingrese nota bien puto putp outo  "))
    cant_alumnos += 1 
    notas_total += nota
    if nota < 4:
        desaprobados += 1 
    else: 
        apronados += 1
    legajos.append(legajo)
    notas.append(nota)
    legajo = int(input("Ingrese legajo "))


promedio = notas_total // cant_alumnos  
print(apronados, desaprobados, promedio )
hola = ordenar_burbuja(notas, legajos)
print(hola)


#for f in range(len(legajos)):
 #   matriz[0].append(legajos[f])
  #  matriz[1].append(notas[f])

#for i in range(len(matriz)):
 #   for j in range(len(matriz)):
  #      print(matriz[i][j])