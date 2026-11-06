from inventario import mostrar_productos, obtener_producto_por_codigo
import datetime

ventas = []
numero_factura = 1

def imprimir_en_termica(texto):
    """Intenta imprimir en tu Xprinter XP-80"""
    # OPCION 1: Por USB directo (la mejor para tickets)
    try:
        from escpos.printer import Usb
        # VID y PID de tu Xprinter XP-80
        p = Usb(0x0416, 0x5011, profile="TM-T88")
        p.set(align='left')
        p.text(texto)
        p.text("\n\n")
        p.cut()
        print(" Factura impresa en Xprinter XP-80")
        return True
    except Exception as e:
        print(f"No se pudo por USB directo: {e}")
        print("Intentando por Windows...")

    # OPCION 2: Por Windows, usando la impresora que ya instalaste
    try:
        import win32api
        import win32print
        # Guarda un temporal para mandar a imprimir
        with open("factura_temp.txt", "w", encoding="utf-8") as f:
            f.write(texto)
        win32api.ShellExecute(0, "print", "factura_temp.txt", '/d:"Xprinter XP-80"', ".", 0)
        print(" Enviado a imprimir por Windows")
        return True
    except Exception as e2:
        print(f" No se pudo imprimir: {e2}")
        print("Instala con: pip install python-escpos pywin32")
        return False

def generar_factura(codigo, producto, cantidad, unidades, nombre_de_tipo, total, pago, cambio):
    global numero_factura
    # ESTA PARTE SACA LA HORA Y FECHA Y HORA EXACTA DE MI PC PARA LA FACTURA
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    # Texto centrado para 80mm (42 caracteres por linea)
    factura_texto = f"""
       FACTURA - PROYECTO MARKET

Factura Nro: {numero_factura}
Fecha: {fecha}

Codigo: {codigo}
Producto: {producto['nombre']}
Tipo de venta: {nombre_de_tipo}
Cantidad vendida: {cantidad}
Unidades descontadas: {cantidad * unidades}
Precio unitario: Bs. {producto['precio']}

Total: Bs. {total}
Pago: Bs. {pago}
Cambio: Bs. {cambio}

       Gracias por su compra!

"""
    print(factura_texto)

    # --- PREGUNTA 1: GUARDAR ---
    guardar = input("¿Desea guardar la factura? (s/n): ").strip().lower()
    if guardar == "s":
        # ESTA PARTE DEL CODIGO CREA UNA CARPETA Y EL APARTADO " UTF_8" ES PARA
        # SALGAN BIEN LAS TILDES Y LA Ñ
        nombre_archivo = f"factura_{numero_factura}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(factura_texto)
        print(f"Factura guardada como {nombre_archivo}")
    else:
        print("Factura no guardada.")

    # --- PREGUNTA 2: IMPRIMIR (NUEVO) ---
    imprimir = input("¿Desea imprimir la factura? (s/n): ").strip().lower()
    if imprimir == "s":
        imprimir_en_termica(factura_texto)
    else:
        print("Factura no impresa.")

    # Solo sube el numero si se guardo o se imprimio, para que no se repita
    if guardar == "s" or imprimir == "s":
        numero_factura += 1

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
            break
            
        elif opcion == "1":
            mostrar_productos()
            codigo = input("\nIngrese el codigo del producto: ").strip()
            producto = obtener_producto_por_codigo(codigo)
            
            
            
            if producto is None:
                print("Producto no encontrado")
                continue
            print("=" * 40)
            print(f"PRODUCTO ENCONTRADO: {producto['nombre']} | Precio: Bs. {producto['precio']} | Stock: {producto['cantidad']}")         
            print("---TIPO DE VENTA---")
            print("1. VENTA POR UNIDAD")
            print("2. VENTA POR CAJA")
            print("=" * 40)
            opcion_venta = input("Selecciona una opcion: ").strip()

            if opcion_venta == "1":
                nombre_de_tipo = "Unidad"
                unidades = 1
            elif opcion_venta == "2":
                nombre_de_tipo = "Caja"
                unidades = producto.get("unidades_por_paquete", 12)
                print(f"Cada caja trae {unidades} unidades")
            else:
                print("Opcion invalida")
                continue

            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("Ingrese un numero entero valido")
                continue

            # Calculamos cuantas unidades reales se van a descontar
            descuento = cantidad * unidades

            if cantidad <= 0 or descuento > producto["cantidad"]:
                print("Cantidad no valida o stock insuficiente")
                continue

            
            total = producto["precio"] * descuento
            print(f"Tipo de venta: {nombre_de_tipo}")
            print(f"Total a pagar: Bs. {total}")

            try:
                pago = float(input("Monto recibido: Bs. "))
            except ValueError:
                print("Ingrese un monto numerico valido")
                continue

            if pago < total:
                print("Pago insuficiente. Venta cancelada.")
                continue

            # Actualizamos stock con DESCUENTO, no con cantidad
            producto["cantidad"] -= descuento
            # Si era por caja, también bajamos los paquetes
            if nombre_de_tipo == "Caja":
                producto["cantidad_paquetes"] = producto.get("cantidad_paquetes", 0) - cantidad

            cambio = pago - total
            print("Venta realizada correctamente")

            # LLAMAMOS A LA FACTURA
            generar_factura(codigo, producto, cantidad, unidades, nombre_de_tipo, total, pago, cambio)

            # GUARDAMOS LA VENTA AQUÍ,
            ventas.append({
                "codigo": codigo,
                "nombre": producto["nombre"],
                "cantidad": cantidad,
                "tipo": nombre_de_tipo,
                "total": total
            })

            if producto["cantidad"] <= 5:
                print("Advertencia: Quedan pocos productos en stock")

        else:
            print("Opcion no valida. Intente de nuevo.")

def mostrar_ventas():
    print("\n===== HISTORIAL DE VENTAS =====")
    if not ventas:
        print("No hay ventas registradas")
        return
    for v in ventas:
        print(f"Codigo: {v['codigo']} | Producto: {v['nombre']} | Cantidad: {v['cantidad']} {v['tipo']} | Total: Bs {v['total']}")