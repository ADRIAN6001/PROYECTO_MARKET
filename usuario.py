from DEFINICIONES import menu_inventario
from ventas import venta

## lista de usaurios
usuarios = [
    {"usuario": "admin", "contraseña": "admin123", "rol": "administrador"},
    {"usuario": "kevin", "contraseña": "12345", "rol": "empleado"},
    {"usuario": "alejandrina", "contraseña": "12345", "rol": "empleado"},
    {"usuario": "adrian", "contraseña": "12345", "rol": "empleado"},
    {"usuario": "ruddy", "contraseña": "12345", "rol": "empleado"}
]

## evita que el nombre tenga numeros
def validar_nombre_tiene_numeros(nombre):
    for letra in nombre:
        if letra.isdigit():
            return True
    return False

## validacion del usuario y su contraseña
def autenticar_usuario(usuario_ingresado, contraseña_ingresada):

    ## evita que el nombre de usaurio contenga numeros
    if validar_nombre_tiene_numeros(usuario_ingresado):
        print("\nALERTA DE ERROR")
        print("El nombre de usuario no puede contener numeros para ingresar.")
        return False, "", ""

    ## validacion segun la lista de usuarios
    for u in usuarios:
        if usuario_ingresado == u["usuario"] and contraseña_ingresada == u["contraseña"]:
            return True, u["rol"], u["usuario"]
            
    return False, "", ""

## menu del empleado
def ejecutar_menu_empleado():
    print("-" * 35)
    print("\n Menu del Empleado")
    print("-" * 35)
    print("1. Gestionar Inventario de Productos")
    print("2. Realizar Ventas")
    print("-" * 35)

    opcion_empleado = input("Seleccione una opcion: ").strip()

    ## abre el inventario de productos
    if opcion_empleado == "1":
        menu_inventario()

    ## abre el modulo de ventas    
    elif opcion_empleado == "2":
        print("Estas son las ventas")
        venta()
    else:
        print("Opcion no valida.")
