# Aqui se guardaran todos los productos
productos = []

# Aqui registramos nuevos productos
def registro_de_productos():
    print("\n" + "=" * 40)
    print("         REGISTRO DE NUEVOS PRODUCTOS")
    print("1. Registrar producto por unidad")
    print("2. Registrar producto por paquete")
    print("=" * 40)
    opcion = input("Ingrese una opcion: ").strip()

    # registro por unidades
    if opcion == "1":
        print("\n  REGISTRO DE PRODUCTOS POR UNIDADES ")
        codigo = input("Ingrese el codigo del producto: ").strip()

        # Verificamos que el codigo no exista
        for p in productos:
            if p["codigo"] == codigo:
                print("Error: Ya existe un producto con ese codigo")
                return

        nombre = input("Ingrese el nombre del producto: ").strip()
        try:
            precio = float(input("Ingrese el precio por UNIDAD: "))
            cantidad = int(input("Ingrese la cantidad (existencias en unidades): "))
        except ValueError:
            print("Error: Precio y cantidad deben ser valores numericos validos.")
            return

        if precio <= 0 or cantidad < 0:
            print("Error: Precio y cantidad deben ser positivos.")
            return

        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,  
            "tipo": "unidad",
            "unidades_por_paquete": 1,
            "cantidad": cantidad,  
            "cantidad_paquetes": 0
        }
        productos.append(nuevo_producto)
        print(f"Producto '{nombre}' registrado exitosamente. Stock: {cantidad} unidades.")

    # registro por paquetes
    elif opcion == "2":
        print("\n  REGISTRO DE PRODUCTOS POR PAQUETES ")
        codigo = input("Ingrese el codigo del producto: ").strip()

        # Verificamos que el codigo no exista
        for p in productos:
            if p["codigo"] == codigo:
                print("Error: Ya existe un producto con ese codigo")
                return

        nombre = input("Ingrese el nombre del producto: ").strip()
        try:
            precio_paquete = float(input("Ingrese el precio del PAQUETE: "))
            unidades_por_paquete = int(input("Cuantas unidades trae cada paquete? Ej: 6, 12: "))
            cantidad_paquetes = int(input("Ingrese la cantidad de PAQUETES: "))
        except ValueError:
            print("Error: Deben ser valores numericos validos.")
            return

        if precio_paquete <= 0 or unidades_por_paquete <= 0 or cantidad_paquetes < 0:
            print("Error: Los valores deben ser positivos.")
            return

        #  convertimos todo a unidades
       
        cantidad_total_unidades = cantidad_paquetes * unidades_por_paquete

        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio_paquete,  # OJO: aqui el precio es POR PAQUETE, no por unidad
            "tipo": "paquete",
            "unidades_por_paquete": unidades_por_paquete,
            "cantidad": cantidad_total_unidades,  # 60
            "cantidad_paquetes": cantidad_paquetes  # 5
        }
        productos.append(nuevo_producto)
        print(f"Producto '{nombre}' registrado: {cantidad_paquetes} paquetes = {cantidad_total_unidades} unidades.")
        print(f"Precio por paquete: Bs. {precio_paquete} | Precio por unidad: Bs. {precio_paquete / unidades_por_paquete:.2f}")

    else:
        print("Opcion no valida.")
def mostrar_productos():
    print("\n" + "=" * 40)
    print("          LISTA DE PRODUCTOS")
    print("=" * 40)
    if not productos:
        print("No hay productos registrados en el inventario.")
        print("=" * 40)
        return

    for p in productos:
        # Usamos .get() por si tienes productos viejos sin estos campos
        tipo = p.get("tipo", "unidad")
        unidades_por_paquete = p.get("unidades_por_paquete", 1)
        cantidad_paquetes = p.get("cantidad_paquetes", 0)

        print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: Bs. {p['precio']}")

        if tipo == "paquete":
            print(f"  -> Tipo: Paquete de {unidades_por_paquete} unidades")
            print(f"  -> Stock: {cantidad_paquetes} paquetes = {p['cantidad']} unidades totales")
        else:
            print(f"  -> Tipo: Por unidad")
            print(f"  -> Stock: {p['cantidad']} unidades")

        # AQUI MISMO LA ALERTA, para que la veas al listar
        if p['cantidad'] < 5:
            print("  ALERTA: STOCK BAJO!")

        print("-" * 40)

    print("=" * 40)
def buscar_producto():
    print("\n" + "=" * 40)
    print("            BUSCAR PRODUCTO")
    print("=" * 40)
    criterio = input("Ingrese el codigo o nombre a buscar: ").strip().lower()
    
    encontrados = [
        p for p in productos 
        if criterio == p["codigo"].lower() or criterio in p["nombre"].lower()
    ]

    if encontrados:
        print(f"Se encontraron {len(encontrados)} coincidencia(s):")
        print("-" * 40)
        for p in encontrados:
            print(f"Código: {p['codigo']}  Nombre: {p['nombre']}  Precio: Bs. {p['precio']} | Cantidad: {p['cantidad']}")
            print("-" * 40)
    else:
        print("No se encontraron productos con ese criterio.")

def modificar_producto():
    print("\n" + "=" * 40)
    print("           MODIFICAR PRODUCTO")
    print("=" * 40)
    codigo = input("Ingrese el código del producto a modificar: ").strip()
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Producto encontrado: {p['nombre']} (Precio: {p['precio']}, Stock: {p['cantidad']})")
            
            nuevo_nombre = input(f"Nuevo nombre (presione Enter para mantener '{p['nombre']}'): ").strip()
            nuevo_precio = input(f"Nuevo precio (presione Enter para mantener '{p['precio']}'): ").strip()
            nueva_cantidad = input(f"Nueva cantidad (presione Enter para mantener '{p['cantidad']}'): ").strip()

            if nuevo_nombre:
                p["nombre"] = nuevo_nombre
            if nuevo_precio:
                try:
                    p["precio"] = float(nuevo_precio)
                except ValueError:
                    print("Precio no valido, se mantiene el anterior.")
            if nueva_cantidad:
                try:
                    p["cantidad"] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad no valida, se mantiene la anterior.")
            
            print("Producto actualizado correctamente.")
            return

    print("No se encontró ningún producto con ese código.")

def eliminar_producto():
    print("--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el codigo del producto a eliminar: ").strip()
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Producto encontrado: {p['nombre']}")
            confirmacion = input("¿Esta seguro de eliminarlo? (s/n): ").strip().lower()
            if confirmacion == 's':
                productos.remove(p)
                print("Producto eliminado exitosamente.")
            else:
                print("Operacion cancelada.")
            return

    print("No se encontro ningun producto con ese codigo.")
def valor_total_inventario():
    print("--- VALOR TOTAL DEL INVENTARIO ---")
    if not productos:
        print("El inventario esta vacio.")
        return
    
    total = sum(p["precio"] * p["cantidad"] for p in productos)
    print(f"El valor total de la mercancía en stock es: Bs. {total:.2f}")
# opcion 6
def alerta_stock_bajo():
    print("\n--- PRODUCTOS CON STOCK BAJO (< 5 unidades) ---")
    limite = 5
    bajos = [p for p in productos if p["cantidad"] < limite]
    
    if not bajos:
        print(" No hay productos con stock bajo.")
        return

    for p in bajos:
        tipo = p.get("tipo", "unidad")
        unidades_por_paquete = p.get("unidades_por_paquete", 1)
        cantidad_paquetes = p.get("cantidad_paquetes", 0)

        if tipo == "paquete":
            print(f" Cód: {p['codigo']} | Nombre: {p['nombre']} | Stock: {p['cantidad']} unidades = {cantidad_paquetes} paquetes de {unidades_por_paquete} (¡REPONER!)")
        else:
            print(f" Cód: {p['codigo']} | Nombre: {p['nombre']} | Cantidad restante: {p['cantidad']} unidades (¡REPONER!)")

def menu_inventario():
    while True:
        print("--- MENU DE INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar producto")
        print("4. Modificar datos de producto")
        print("5. Eliminar producto")         
        print("6. Ver alertas de stock bajo")   
        print("7. Ver valor total del inventario")
        print("8. Salir")
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            registro_de_productos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            alerta_stock_bajo()
        elif opcion == "7":
            valor_total_inventario()
        elif opcion == "8":
            print("Saliendo del modulo de inventario...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
if __name__ == "__main__":
    menu_inventario()

def obtener_producto_por_codigo(codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None
