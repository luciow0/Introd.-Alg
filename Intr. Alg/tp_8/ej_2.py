depas = []
tamaño = []

total_exp = 0


def busqueda(lista, elemento_buscado):
    pos = -1 
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == elemento_buscado:
            pos = i
        i += 1
    return pos
   

""""el problema era literalmente el menor igual (<=) del while del algoritmo de busqueda, si le pones i <= len arroja error, si le pones i < len no. que mierda se yo estas mugres de la compu andan asi """
"""para inccovar a una funcion con un valaor de retorno, en este caso pos, es necesario declararla nuevamente fuera de la funcion ya que la variable por si solo es local de la funcion"""

j = 0

while j < 20:
    unidad = int(input("Ingrese el numero de unidad de su depa "))

    pos = busqueda(depas, unidad)

    if pos == -1:
        depas.append(unidad)
        metros = float(input("Ingrese el tamaño de su depa en metros cuadrados "))
        tamaño.append(metros)
        precio = float(input("Ingrese el precio por metro cuadrado del depa "))

        j += 1 
        

    else:
        print(f"departamento ya inluiddo en la lista, posicion {pos}")

    total_exp += precio * metros


promedio = total_exp / 20

def bubble_sort(depas, tamaño):
    n = len(tamaño)
    for i in range(n):
        for j in range(0, n-i-1):
            if tamaño[j] < tamaño[j+1]:
                tamaño[j], tamaño[j+1] = tamaño[j+1], tamaño[j]
                depas[j], depas[j+1] = depas[j+1], depas[j]

    return depas, tamaño

print(f"promdio de expensas {promedio}")

""""basicamente la funcion bubble, primero que nada tiene que tener un return para devovler las listas ordenadas"""

depas_ordenado , tamaño_ordenado = bubble_sort(depas, tamaño) ##se puede invocar a la funcion con las dos nuevas variables que contendran las listas


matriz = [ depas_ordenado , tamaño_ordenado]

"""esto crea una matriz con las dos listas"""

for fila in matriz:
    print(fila)

    """"y esto imprime elemento por elemento de matriz """





