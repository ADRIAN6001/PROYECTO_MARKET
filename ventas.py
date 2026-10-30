from DEFINICIONES import mostrar_productos, buscar_producto

def venta():
    print("\n" + "=" * 40)
    print("          MÓDULO DE VENTAS          ")
    print("=" * 40)

    mostrar_productos()
    codigo = input("\nIngrese el código del producto: ")

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
    cambio= pago - total
    print("Venta realizada correctamente")
    
    print("\n========================================")
    print("          COMPROBANTE DE VENTA          ")
    print("========================================")

    print(f"Codigo: {codigo}")
    print(f"Producto: {producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precion unitario : {producto} bs")
    print(f"Total en bs. : {total}")
    print(f"Pago en bs.: {pago}")
    print(f"Cambio en bs. : {cambio}")

    print("\n========================================")
    print("       ¡Gracias por su compra!          ")
    print("========================================")

    venta()