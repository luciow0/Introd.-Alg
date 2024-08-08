for i in range (1, 11):
   
    num = int(input())

    nums = num

    if i == 1:
        mayor = num
        pos = i

    elif num > mayor:
        mayor = num
        pos = i
    
    i += 1

print("promedio de los numeros",nums / 10, "mayor de los numeros", mayor, "Ingresado en la posicion ", pos)