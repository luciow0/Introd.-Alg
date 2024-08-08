suma = 0
total = 0

if suma <= 100:
    nums = int(input("ingrese numeros"))

    while suma <= 100:
        if nums % 2 == 0:
            suma += nums
            total += nums
        else:
            total += nums
    
        nums = int(input("ingrese numeros"))

print(total)

    