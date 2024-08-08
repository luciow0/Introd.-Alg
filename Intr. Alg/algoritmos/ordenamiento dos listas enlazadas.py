def burbujeo(legajos, notas):
    largo = len(legajos)
    desordenada = True
    while desordenada: 
        desordenada = False
        for i in range(largo-1):
            if notas[i]<notas[i+1]:
                aux = notas[i]
                notas[i] = notas[i+1]
                notas[i+1] = aux
                aux = legajos[i]
                legajos[i] = legajos[i+1]
                legajos[i+1] = aux
                desordenada = True



listanotas = [] 
listalegajos = []

lu = int(input("Legajo? (-1 para finalizar)"))

while lu!= -1:
    nota = int(input("Clasificacion? "))
    listalegajos.append(lu)
    listanotas.append(nota)
    lu = int(input("Legajo? (-1 para finalizar)"))

burbujeo(listalegajos, listanotas)

print( )

for i in range(len(listalegajos)):
    print(listalegajos[i], ": ", listanotas[i], sep="")


##sep= El parámetro sep indica qué carácter se va a utilizar para separar los distintos objetos que se imprimirán en la pantalla. Por defecto es el espacio en blanco.
##end= "end" es un parámetro opcional que se puede pasar a la función de impresión en Python. Este parámetro especifica el carácter o la cadena que se utilizará para finalizar la línea después de imprimir el contenido especificado.

