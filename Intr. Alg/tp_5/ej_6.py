n = int(input("Ingrese "))
if n < 0:
    n *= -1
print(n)
cifras = 0
while n > 0:
    n //= 10 
    cifras += 1 
print(cifras)