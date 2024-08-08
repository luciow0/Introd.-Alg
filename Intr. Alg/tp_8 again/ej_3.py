N = int(input("Ingrese la cantidad de competidores "))
while N < 1: 
    N = int(input("Ingrese la cantidad de competidores valida "))
competidores = []
 
numer_comp = int(input("Ingrese el numero de competidor  "))  
    
while len(competidores) <= N:
    if numer_comp < 1: 
        numer_comp = int(input("Ingrese un numero de competidor valido "))
    else:
        competidores.append(numer_comp)
    
    numer_comp = int(input("ingrese el siguiente numero de competidor"))
