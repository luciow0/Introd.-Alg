# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Inicializamos un contador de dígitos en 0
contador_digitos = 0

# Si el número es negativo, convertimos su valor absoluto para contar los dígitos
if numero < 0:
    numero = abs(numero)

# Mientras el número no sea 0, incrementamos el contador y dividimos el número entre 10 para eliminar un dígito
while numero != 0:
    contador_digitos += 1
    numero //= 10

# Imprimimos la cantidad de dígitos
print("El número ingresado tiene", contador_digitos, "dígitos.")
