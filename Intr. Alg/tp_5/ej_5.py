def ver_si_es_bisiesto(año):
    bisiesto = False

    if año % 4 == 0 and año % 100 != 0: 
        bisiesto =  True

    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
        bisiesto = True

    return bisiesto

def evaluar_limite(mes):
    if mes == 4 or mes == 6 or mes == 9 or mes == 11: 
        limite = 30     
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
        limite = 31
    elif mes == 2: 
        lol = ver_si_es_bisiesto(año)
        if lol: 
            limite = 29 
        else: 
            limite = 28
    return limite

dia = int(input("Ingrese dia "))
mes = int(input("Ingrese mes ")) 
año = int(input("Ingrese año "))

N = int(input("Ingrese dias a sumar "))
ver_limite = evaluar_limite(mes)

for i in range(N): 
    if dia < ver_limite: 
        dia += 1
    else: 
        if mes < 12: 
            mes += 1
            ver_limite = evaluar_limite(mes)
            dia = 1
        elif mes == 12: 
            mes = 1
            ver_limite = 31
            dia = 1 
            año += 1
    
print(dia, mes, año)

