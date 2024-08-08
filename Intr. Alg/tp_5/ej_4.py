importe = int(input("ingrese el importe de su factura ")) 
dia_en_que_pago = int(input("ingrese el dia en que el pago fue efectuado entre 1 y 31"))
while dia_en_que_pago < 1 or dia_en_que_pago > 31: 
    dia_en_que_pago = int(input("por favor ingrese un numero entre 1 y 31"))
    
if dia_en_que_pago <= 10: 
    if importe > 10000: 
        importe_orig = importe
        importe = importe * 0.98 
        print("El importe a abonar se le aplico un descuento del 2% su factura paso de valer", importe_orig, "a", importe)
    
    else: 
        importe_orig = importe
        importe -= 200 
        print("El importe a abonar se le aplico un descuento de 200$ su factura paso de valer", importe_orig, "a", importe)
    
elif dia_en_que_pago > 10 and dia_en_que_pago <= 20: 
    print("importe a pagar", importe)


elif dia_en_que_pago < 20: 
    if importe > 3500: 
        importe_orig = importe
        multa = importe * 0.10
        importe = importe + multa
        print(multa, importe, importe_orig)

    else: 
        print("importe original ", importe)
        importe += 350 
        print("importe a abonar con multa aplicada ", importe)