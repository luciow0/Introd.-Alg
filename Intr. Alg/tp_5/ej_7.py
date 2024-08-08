def contar_cifras(numero):
    # Cuenta la cantidad de cifras de un número
    contador = 0
    temp = numero
    while temp > 0:
        temp //= 10
        contador += 1
    return contador

def es_narcisista(numero):
    num_cifras = contar_cifras(numero)
    suma = 0
    temp = numero
    while temp > 0:
        digito = temp % 10
        print(digito)
        suma += digito ** num_cifras
        temp //= 10
    return suma == numero

lol = es_narcisista(153)
print(lol)