filas = int(input("Ingrese "))
columnas  = int(input("Ingrese "))
matriz = []
for f in range(filas): 
    matriz.append([])
    print (matriz)
    for c in range(columnas):
        matriz[f].append(0)
        print (matriz)
print (matriz)

#for fila in range(0,len(matriz)): 
 #   for columna in range(0,len(matriz)): 
  #      print("[", fila, "] [",columna, "] ->", 
   #           matriz[fila][columna])
        
for f in range(filas):
    for c in range(columnas): 
        print("ingrese el numero que desea agregar en ", ([f],[c]))
        n = int(input(" "))
        matriz[f][c] = n 

for f in range(filas): 
    for c in range(columnas): 
        print(matriz[f][c], end=" ")
    print( )

