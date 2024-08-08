total_personas = 0 
cantidad_menores_edad = 0
cantidad_mayores_edad = 0
suma_menores = 0
suma_mayores = 0
edad_mayor_mayores = 0
edad_mayor_menores = 0
bebes = 0
edades_erroneas = 0

edad = (int(input("ingrese su edad (-1 para finalizar)")))

while (edad != -1):

    if (edad < 0 or edad > 100):
        edades_erroneas += 1

    else:
        total_personas += 1

        if edad < 18:
            cantidad_menores_edad += 1
            suma_menores += edad
            if edad > edad_mayor_menores:
                edad_mayor_menores = edad
    
            if edad < 2:
                bebes += 1

        elif edad >= 18:
            cantidad_mayores_edad += 1
            suma_mayores += edad
            if edad > edad_mayor_mayores:
                edad_mayor_mayores = edad

    edad = int(input("ingrese su edad (-1 para finalizar)"))

if total_personas > 0:
    print(f"cantidad de personas ingresadas {total_personas}")

    if cantidad_menores_edad > 0:
        print(f"cantidad de menores {cantidad_menores_edad} promedio de edad {suma_menores / cantidad_menores_edad} mayor edad del grupo {edad_mayor_menores}")
        print(f"cantidad de bebes {bebes}")

    if cantidad_mayores_edad > 0:
        print(f"cantidad de mayores {cantidad_mayores_edad} promedio de edad {suma_mayores / cantidad_mayores_edad} mayor edad del grupo {edad_mayor_mayores}")

print(f"cantidad de edades erroneas {edades_erroneas}")

