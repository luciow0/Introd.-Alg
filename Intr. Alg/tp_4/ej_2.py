num = int(input("ingrese sus nums, -1 para finalizar"))
numeros = 0
i = 0
while num != -1:
    numeros += num
    i = (i + 1) % 2
    num = int(input("Ingrese sus nums, -1 para finalizar"))


if i == 0:
    print ("cantidad de numeros par")

else:
    print("cantidad de numeros impar")