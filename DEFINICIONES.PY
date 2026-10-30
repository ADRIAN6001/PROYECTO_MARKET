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

def eliminar_producto():
    print("--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Producto encontrado: {p['nombre']}")
            confirmacion = input("¿Está seguro de eliminarlo? (s/n): ").strip().lower()
            if confirmacion == 's':
                productos.remove(p)
                print("Producto eliminado exitosamente.")
            else:
                print("Operación cancelada.")
            return

    print("No se encontró ningún producto con ese código.")
def valor_total_inventario():
    print("--- VALOR TOTAL DEL INVENTARIO ---")
    if not productos:
        print("El inventario está vacío.")
        return
    
    total = sum(p["precio"] * p["cantidad"] for p in productos)
    print(f"El valor total de la mercancía en stock es: Bs. {total:.2f}")

def alerta_stock_bajo():
    print("--- PRODUCTOS CON STOCK BAJO (< 5 unidades) ---")
    limite = 5
    bajos = [p for p in productos if p["cantidad"] < limite]
    
    if not bajos:
        print(" No hay productos con stock bajo.")
        return

    for p in bajos:
        print(f" Cód: {p['codigo']} | Nombre: {p['nombre']} | Cantidad restante: {p['cantidad']}")


def menu_inventario():
    while True:
        print("--- MENÚ DE INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar producto")
        print("4. Modificar datos de producto")
        print("5. Eliminar producto")         
        print("6. Ver alertas de stock bajo")   
        print("7. Ver valor total del inventario")
        print("8. Salir")
        
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
            eliminar_producto()
        elif opcion == "6":
            alerta_stock_bajo()
        elif opcion == "7":
            valor_total_inventario()
        elif opcion == "8":
            print("Saliendo del módulo de inventario...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    menu_inventario()
   