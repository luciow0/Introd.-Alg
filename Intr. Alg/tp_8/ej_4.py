import random
num_aleatorio = random.randint(999, 9999)
intentos = 0
mejores_jugadores = [45947502, 87987444, 34567890, 12345678, 89, 78]
mejores_marcas = [2, 3, 7, 10, 200, 79009]
jugar = True


while jugar == True:

    num_ing = int(input("ingrese un numero de 4 cifras para adivinar el numero aleatorio, -1 para abandonar "))


    """  LE ERRO  """

    while (num_ing != num_aleatorio and num_ing != -1):

        intentos += 1

        if num_ing < num_aleatorio:
            print("el numero ingresado es menor al numero buscado")

        else:
            print("el numero ingresado es mayor al numero buscado")

        num_ing = int(input("ingrese un numero de 4 cifras para adivinar el numero aleatorio, -1 para abandonar "))


    """"  LE PEGO  """

    if num_ing == num_aleatorio:

        intentos += 1

        mejor = mejores_marcas[0]

        if intentos < mejor:
            aux = mejor
            mejor_marca = intentos
            print(f"felicitaciones! el numero ingresado {num_ing} es el numero buscado, cantidad de intentos {intentos}, usted ha superado la mejor marca actual {aux}")

            dni = int("ingrese su numero de DNI para dejar registrada su marca ")

            mejores_jugadores.append(dni)
            mejores_marcas.append(mejor_marca)
    
        else:
            print(f"felicitaciones! el numero ingresado {num_ing} es el numero buscado, cantidad de intentos {intentos}")

    
    def bubble_sort(mejores_jugadores, mejores_marcas):
        n = len(mejores_jugadores)
        for i in range(n):
            for j in range(0, n-i-1):
                if mejores_marcas[j] < mejores_marcas[j+1]:
                    mejores_marcas[j] , mejores_marcas[j+1] = mejores_marcas[j+1] , mejores_marcas[j]
                    mejores_jugadores[j] , mejores_jugadores[j+1] = mejores_jugadores[j+1] , mejores_jugadores[j]

    matriz = mejores_jugadores, mejores_marcas
    print(matriz)

    seguir_jugando = int(input("Deseas seguir jugando? ingresa 1 para seguir jugando o 0 para abandonar"))

    if seguir_jugando == 1:
        jugar = True
    
    elif seguir_jugando == 0:
        jugar = False



        
