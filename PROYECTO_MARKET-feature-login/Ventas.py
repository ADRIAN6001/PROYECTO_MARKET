from inventario import mostrar_inventario, buscar_producto
def venta():
    mostrar_inventario()
    codigo = input("Código del producto: ")
    producto = buscar_producto(codigo)
    if producto is None:
        print("Producto no encontrado")
        return
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Ingrese un número entero")
        return
    if cantidad <= 0 or cantidad > producto["cantidad"]:
        print("Cantidad no válida o stock insuficiente")
        return
    
    total = producto["precio"] * cantidad
    print("Total a pagar: Bs",total)

    try:
        pago = float(input("Monto recibido: Bs "))
    except ValueError:
        print("Ingrese un monto válido")
        return
    if pago < total:
        print("Pago insuficiente")
        return
    producto["cantidad"] -= cantidad
    cambio= pago -total
    print("Venta realizada correctamente")
    print("Cambio: Bs", cambio)