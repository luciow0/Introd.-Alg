num = int(input("ingrese su num, -1 para finalizar"))
i = 0
nums = 0

while num != -1:

    if i == 0:
        mayor= num
        menor = num

    if num > mayor:
        mayor = num
    
    if num < menor:
        menor = num
        
    nums += num
    i += 1
    num = int(input("ingrese su num"))

print(f"menor {menor} mayor {mayor}")
