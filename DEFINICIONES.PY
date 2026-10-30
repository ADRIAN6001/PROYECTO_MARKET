# Aqui se guardaran todos los  productos
productos=[]



# Aqui registramos nuevos productos
def registro_de_productos():
    print("\n" + "=" * 40)
    print("         REGISTRO DE NUEVOS PRODUCTOS")
    print("\n" + "=" * 40)
    codigo = input("Ingrese el código del producto: ").strip()
    
    # Verificar si el código ya existe en codigo
    for p in productos:
        # p es una simple variable
        if p["codigo"] == codigo:
            print("Error: Ya existe un producto con ese código")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad (existencias): "))
    except ValueError:
        print("Error: Precio y cantidad deben ser valores numéricos válidos.")
        return
# Diccionario donde se guardan todos los productos
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' registrado exitosamente.")

def mostrar_productos():
    print("\n" + "=" * 40)
    print("          LISTA DE PRODUCTOS")
    print("=" * 40)
    if not productos:
        print("No hay productos registrados en el inventario.")
        print("=" * 40)
        return

    for p in productos:
        print(f" Código: {p['codigo']}  Nombre: {p['nombre']}  Precio: Bs. {p['precio']}  Cantidad: {p['cantidad']}")
    print("=" * 40)

def buscar_producto():
    print("\n" + "=" * 40)
    print("            BUSCAR PRODUCTO")
    print("=" * 40)
    criterio = input("Ingrese el código o nombre a buscar: ").strip().lower()
    
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
                    print("Precio no válido, se mantiene el anterior.")
            if nueva_cantidad:
                try:
                    p["cantidad"] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad no válida, se mantiene la anterior.")
            
            print("Producto actualizado correctamente.")
            return

    print("No se encontró ningún producto con ese código.")

def menu_inventario():
    while True:
        print("\n" + "=" * 35)
        print("         MENÚ DE INVENTARIO")
        print("=" * 35)
        
        print("1. Registrar producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar producto")
        print("4. Modificar datos de producto")
        print("5. Volver / Salir")
        print("=" * 35)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registro_de_productos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            print("Saliendo del módulo de inventario...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_inventario()
   