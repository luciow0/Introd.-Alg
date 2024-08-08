n = int(input("ingrese la cantidad de competidores "))

competidores = []
tiempo = []
tiempo_total = 0

def pasar_segundos(segundos):
    horas = segundos // 3600
    minutos = horas // 60
    segundos_restantes = segundos % 60

    return [horas , minutos , segundos_restantes]



for i in range (0, n-1):

    numero_competidor = int(input("ingrese el numero del competidor "))
    competidores.append(numero_competidor)

    segundos = float(input("ingrese la cantidad de segundos "))

    tiempo_total += segundos

    if i == 0:
        ganador = numero_competidor
        tiempo_min = segundos

    else: 
        if segundos < tiempo_min:
            ganador = numero_competidor
            tiempo_min = segundos

    

    tiempo = pasar_segundos(segundos)

    

print(f"el ganador de la carrera es {ganador} con un tiempo de {tiempo_min}")

promedio = tiempo_total / n
print(f"promedio de tiempo de los ciclistas {promedio}")

record = int(input("ingrese el record de la carrera anterior en segundos "))

if tiempo_min < record:
    print(f"el competidor {ganador} batio el record anterior de {record} con un tiempo de {tiempo_min}")

else:
    print(f"el tempo record continua sindo {record}")






