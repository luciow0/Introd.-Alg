cantidad = int(input("Ingrese la cant del prod "))
cant_total_ventas = 0
ventas_10_off = 0
ventas_base = 0

while cantidad != -1: 
    precio = int(input("Ingrese el precio del prod por unidad "))

    cant_total_ventas += cantidad

    if cantidad > 100:
        cantidad -= 100
        valor = (12 * precio) + ((88 * precio) * 0.90) + ((cantidad * precio) * 0.75)  
        ventas_10_off += 88
        ventas_base += 12
        print("valor total de la venta: ", valor, "precio promedio por unidad: ", (valor / cantidad))

    elif cantidad > 12 and cantidad < 100: 
        cantidad -= 12
        ventas_10_off += cantidad
        ventas_base += 12
        valor = (12 * precio) + ((cantidad * precio) * 0.90)
        print("valor total de la venta: ", valor, "precio promedio por unidad: ", (valor / cantidad))

    elif cantidad < 12: 
        valor = (cantidad * precio)
        ventas_base += cantidad
        print("valor total de la venta: ", valor, "precio promedio por unidad: ", (valor / cantidad))

    cantidad = int(input("Ingrese  la cant del prod "))

print("cantidad total de ventas ", cant_total_ventas, "cantidad de venta con 10% off ", ventas_10_off, "cantidad de ventas precio base", ventas_base)