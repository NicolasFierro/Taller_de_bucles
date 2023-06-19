

factura_monto = float(input("favor de ingresar los montos de la factura (para finalizar el proceso por favor introduce 0): "))
total = 0
while factura_monto != 0:
    total += factura_monto
    factura_monto = float(input("Ingrese el monto de la siguiente factura (Ingrese 0 para finalizar): "))
if total > 1000:
    descuento = total * 0.1
    total -= descuento
    print(f"el total seria: {total} con un descuento del 10% por haber superado los $1000 en ventas.")
else:
    print(f"El total a pagar es: {total}")