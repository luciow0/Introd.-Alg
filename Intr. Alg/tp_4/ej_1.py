num = int(input("ingresar numero entero"))
numeros = 0

while num != -1:
    
    if numeros == 0:
        primer_numero = num
        numeros += num
    
    numeros += num
    ultimo_numero =num

    num =int(input("Ingrese numero entero"))

print(f"primer num {primer_numero} ultimo numero {ultimo_numero} total {numeros}")