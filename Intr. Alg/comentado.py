# Fence Jumper
from time import sleep 

# Función principal de inicio del juego
def initGame():
    userName = ''
    jumperHeight = 0
    fenceList = []
    
    # Mensaje de bienvenida con un gráfico en ASCII
    print("\n\n ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗\n░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝\n░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░\n░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░\n░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗\n░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
    print("\nWelcome New Player!! (ノ ͡❛ ͜ʖ ͡❛)ノ \nBefore we start, please provide your name so we can save your progress!\n")
    
    # Pausa para simular espera
    sleep(2)
    
    # Bucle para asegurar que el usuario ingrese un nombre válido
    while(len(userName) <= 0):
        userName = str(input("Enter your name: "))
        if(len(userName) <= 0):
            print("Please provide a valid name")
    
    # Llamada a la siguiente fase de configuración del juego
    return gamePreConfigs(jumperHeight, fenceList, userName)

# Función para configurar los parámetros del juego
def gamePreConfigs(jumperHeight, fenceList, userName):
    sleep(0.5)
    print("\nNice to meet you " + userName + "! \nPlease provide some values to get into the game!")
    sleep(1)
    
    # Solicitud de la altura de salto del personaje
    jumperHeight = int(input("Character Jump Height: "))
    fenceInsertingFlag = True
    print("\nEach fence height (Stop adding by entering -1):")
    
    # Bucle para ingresar alturas de vallas
    while(fenceInsertingFlag): 
        fenceInsert = int(input("Fence " + str(len(fenceList) + 1) + ":  "))
        if(fenceInsert < 0):
            if(fenceInsert == -1):
                if(len(fenceList) > 0):
                    print("Finalizing Fence input...")
                    fenceInsertingFlag = False
                    sleep(1)
                else:
                    print("Por favor ingrese al menos 1 valla")
            else:
                print("The input " + str(fenceInsert) + " is not Valid! (Must be positive or 0)")
        else:
            fenceList.append(fenceInsert)
    
    # Llamada a la función para correr el juego
    return runGame(jumperHeight, fenceList, userName)

# Función principal del juego donde el personaje salta las vallas
def runGame(jumperHeight, fenceList, userName):
    potionsUsed = 0
    potionPerFence = []
    maxHeight = 0
    totalFenceHeight = 0
    
    print("\nThe Game is Starting..\n\n")
    sleep(1)
    
    # Bucle a través de cada valla para determinar si se necesitan pociones para saltar
    for index in range(len(fenceList)):
        if(len(potionPerFence) > 2):
            jumperHeight = jumperHeight - potionPerFence[index-3]
        if(jumperHeight < fenceList[index]):
            potionPerFence.append((fenceList[index] - jumperHeight))
            potionsUsed += potionPerFence[index]
            jumperHeight = fenceList[index]
            print("Jumper had to use " + str(potionPerFence[index]) + " potions to jump Fence " + str(index + 1))
        else:
            potionPerFence.append(0)
            print("Potions were not used in Fence " + str(index+1))
        if(fenceList[index] > maxHeight):
            maxHeight = fenceList[index]
        totalFenceHeight += fenceList[index]
        sleep(0.5)
    
    # Llamada a la función para mostrar la información final del juego
    return postGameInfo(potionsUsed, potionPerFence, userName, maxHeight, totalFenceHeight)

# Función para mostrar la información final del juego
def postGameInfo(potionsUsed, potionPerFence, userName, maxHeight, totalFenceHeight):
    noPotionsUsed = 0
    
    # Mensaje de felicitación con un gráfico en ASCII
    print("░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗░██████╗\n██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝\n██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░╚█████╗░\n██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░░╚═══██╗\n╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██████╔╝\n░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░ \n\nCongratulations " + userName + "!\nThese are your stats: ")
    
    # Mostrar estadísticas del juego
    if(potionsUsed == 0):
        print("The Jumper did not use any potions")
    else:
        print("\nPociones totales usadas: " + str(potionsUsed) + "\n")
        for i in range(len(potionPerFence)):
            print("Potions used on Fence " + str(i+1) + ": " + str(potionPerFence[i]))
        noPotionsUsed = 1

    print("\nCantidad de vallas: ", len(potionPerFence))
    print("Altura Máxima: ", maxHeight)
    print("Promedio de altura de vallas: ", (totalFenceHeight/len(potionPerFence)))
    return noPotionsUsed
    
# Programa Principal
print("El programa ha devuelto:", initGame())
