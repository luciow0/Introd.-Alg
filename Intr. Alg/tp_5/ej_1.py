edad = int(input("Ingrese "))
edades_total = 0
cant_personas = 0
mayores_18 = 0
menores_18 = 0
invalidas = []
while edad != -1: 
    if edad > 0 and edad < 100: 
        edades_total += edad
        cant_personas += 1
        if edad > 18: 
            mayores_18 += 1
        else: 
            menores_18 += 1
    else: 
        invalidas.append(edad)

    edad = int(input("Ingrese "))
    


print(edades_total, cant_personas, mayores_18, menores_18, (edades_total // cant_personas), invalidas)