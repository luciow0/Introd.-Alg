cant_des = 0
cant_aprob = 0
notas_total = 0

legajo = int(input("Ingrese su legajo "))
nota = int(input("Ingrese su nota "))

alum = []
notas = []
notas_sup = []
legaj_sup = []

"""comparar primero nota y ultimo la condicion de break"""

while (nota <= 10 and nota >=1 and legajo != -1):

    
        alum.append(legajo)
        notas.append(nota)
        notas_total += nota


        if nota >= 4:
            cant_aprob += 1

        else:
            cant_des += 1

    
    
        legajo = int(input("Ingrese su legajo "))

        if legajo != -1:

            nota = int(input("Ingrese su nota "))

            
##sacar afuera promedio 

prom = len(notas) / notas_total    

i = 0

while i <= (len(notas) -1):
    if notas[i] > prom:
        notas_sup.append(notas[i])
        legaj_sup.append(alum[i])

    i +=1 

print(f"la cantidad de alumnos aprobados es de {cant_aprob}, la cantidad de alumnos desaprobados es de {cant_des}, el promedio de notas es de {prom:.2f}, los alumnos que superan el promedio corresponden a los siguientes legajos {legaj_sup}")



def bubble_sort(alum, notas):
    n = len(notas)
    for i in range(n):
        for j in range(0, n-i-1):
            if notas[j] < notas[j+1]:
                notas[j], notas[j+1] = notas[j+1], notas[j]
                alum[j], alum[j+1] = alum[j+1], alum[j]


print(f"notas en orden ascendente con legajo {alum} {notas}")

matriz = [ alum , notas]

"""la matriz se puede indexar para acceder a cada una de las listas"""

for fila in matriz:
    print(fila)
