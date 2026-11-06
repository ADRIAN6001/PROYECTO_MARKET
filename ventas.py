from inventario import mostrar_productos, obtener_producto_por_codigo

# bucle para el modulo de ventas
ventas=[]
def venta():
    while True:
        print("\n" + "=" * 40)
        print("          MODULO DE VENTAS          ")
        print("=" * 40)
        print("1. Realizar una venta")
        print("2. Volver al menu principal")
        print("=" * 40)
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "2":
            print("Saliendo del modulo de ventas...")

            # cierra el bucle y vuelve al menu principal
            break
            
        elif opcion == "1":
            mostrar_productos()
            codigo = input("\nIngrese el codigo del producto: ").strip()

            # obtiene el producto por su codigo
            producto = obtener_producto_por_codigo(codigo)
            
            if producto is None:
                print("Producto no encontrado")
                continue

            #  eleccion del tipo de venta
            print("---TIPO DE VENTA--")
            print("1. VENTA POR UNIDAD")
            print("2. VENTA POR CAJA")
            opcion=int(input("Selecciona una opcion: "))
            if opcion==1:
                nombre_de_tipo="Unidad"
                unidades=1
            elif opcion==2:
                nombre_de_tipo= "Caja"
                unidades = 12
            else:
                print("opcion invalida")
                continue

            # valida que el numero ingresado sea entero
            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("Ingrese un numero entero valido")
                continue

            #calcula lasa unidades que se descontara
            descuento=cantidad*unidades

            #validacion de nuemero positivos y stok disponible
            if cantidad <=0 or descuento > producto ["cantidad"]:
                print("Cantidad no valida o stok insuficiente")
                continue

            #calculo segun el tipo de producto
            total=producto["precio"]*descuento
            print("Tipo de venta: ",nombre_de_tipo)
            print("Total a pagar: ",total ,"Bs.")

            # validacion en cuanto a numero positivo y stock disponible
            if cantidad <= 0 or descuento > producto["cantidad"]:
                print("Cantidad no valida o stock insuficiente")
                continue 
                
            total = producto["precio"] * cantidad
            print("Total a pagar: Bs. ", total)

            #valida que el monto ingresado sea real
            try:
                pago = float(input("Monto recibido: Bs. "))
            except ValueError:
                print("Ingrese un monto numerico valido")
                continue

            # valida que el pago sea suficiente
            if pago < total:
                print("Pago insuficiente. Venta cancelada.")
                continue

            # actualiza la cantidad del producto en el inventario y calcula el cambio
            producto["cantidad"] -= cantidad
            cambio = pago - total
            print("Venta realizada correctamente")

            # muestra el comprobante de venta
            print("\n========================================")
            print("          COMPROBANTE DE VENTA          ")
            print("========================================")

            print("Codigo: ", codigo)
            print("Producto: ", producto["nombre"])
            print("Cantidad: ", cantidad)
            print("Precio unitario: Bs. ", producto["precio"])
            print("Total en Bs.: ", total)
            print("Pago en Bs.: ", pago)
            print("Cambio en Bs.: ", cambio)

            print("\n========================================")
            print("       Gracias por su compra!          ")
            print("========================================")
        else:
            print("Opcion no valida. Intente de nuevo.")

            ventas.append({
                "codigo": codigo,
                "cantidad": cantidad,
                "total": total
            })
            if producto["cantidad"] <= 5:
                print("Advertencia: Quedan pocos productos en stock")

def mostrar_ventas():
    print("\n===== HISTORIAL DE VENTAS =====")

    for venta in ventas:
        print("Codigo:", venta["codigo"])
        print("Cantidad:", venta["cantidad"])
        print("Total: Bs", venta["total"])
