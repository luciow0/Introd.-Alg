patente = int(input("ingrese la terminacion de la patente del auto, -1 para finalizar "))
autos_pares = 0
autos_impares = 0


while patente != -1:
    if patente % 2 == 0:
        autos_pares += 1
    
    else:
        autos_impares += 1

print("cantidad de autos impares que pasaron", autos_impares ,"cantidad de autos pares que pasaron", autos_pares)