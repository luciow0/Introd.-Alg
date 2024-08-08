import random
n = int(input("Ingrese "))

secuencias = []
sumador = 0
for i in range(n): 
    aux = random.randint(1,20)
    if sumador + aux > 20:
        secuencias.append(0)
        sumador = 0
    sumador += aux
    secuencias.append(aux)

secuencias.append(0)

print(secuencias) 
mas_larga = []
subslita = []

for i in range(len(secuencias)): 
    if secuencias[i] != 0: 
        subslita.append(secuencias[i])
    else: 
        if len(subslita) > len(mas_larga): 
            mas_larga = subslita
        subslita = []
        
if len(subslita) > len(mas_larga):  
    mas_larga = subslita

print(mas_larga)