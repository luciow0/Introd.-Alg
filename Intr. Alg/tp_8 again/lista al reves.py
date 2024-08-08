m = int(input("Ingrese la longitud del numero "))
num = []
for i in range(m):
    print("ingrese la cifra ", [i + 1])
    n = int(input(" "))
    num.append(n)
print(num)

numreves = []
n = len(num)
for j in range(n): 
    numreves.append(num[n -j - 1])
    

print(numreves)