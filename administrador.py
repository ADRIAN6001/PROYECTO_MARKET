from inventario import menu_inventario
from ventas import venta
import usuario 

## menu del administrador
def ejecutar_menu_admin():
    print("-" * 35)
    print("\n Menu del administrador")
    print("-" * 35)
    print("1. Registrar nuevo usuario (Empleado o Admin)")
    print("2. Borrar un usuario existente")
    print("3. Registro de inventario")
    print("4. Ventas")
    print("5. Mostrar lista de empleados")
    print("-" * 35)

    opcion_admin = input("Seleccione una opcion: ").strip()

    if opcion_admin == "1":
        nuevo_usuario = input("Ingrese el nombre del nuevo usuario: ").strip()

        ## validacion en cuanto a numeros en el usuario y si ya existe en lista
        if usuario.validar_nombre_tiene_numeros(nuevo_usuario):
            print("\nERROR")
            print("El nombre de usuario no puede contener numeros")

        ## evita que se repitan los nombres    
        else:
            usuario_repetido = False
            for u in usuario.usuarios:
                if u["usuario"] == nuevo_usuario:
                    usuario_repetido = True
                    break

            if usuario_repetido:
                print("\nERROR")
                print("Este nombre de usuario ya existe en el sistema. Intente con otro.")
            
            ## asignacion de rol con contraseña   
            else:
                print("\nSeleccione el rol para el nuevo usuario:")
                print("1. Administrador")
                print("2. Empleado")
                opcion_rol = input("Seleccione una opcion: ").strip()

                if opcion_rol == "1":
                    rol_asignado = "administrador"
                else:
                    rol_asignado = "empleado"

                nueva_contraseña = input("Ingrese la contraseña: ")

                # asigna los datos del nuevo usaurio en un diccionario
                nuevo_usuario_añadido = {
                    "usuario": nuevo_usuario,
                    "contraseña": nueva_contraseña,
                    "rol": rol_asignado
                }

                ## añade el nuevo usuario a la lista de usuarios
                usuario.usuarios.append(nuevo_usuario_añadido)
                print("Nuevo usuario añadido exitosamente.")

    # elimina un usuario a peticion
    elif opcion_admin == "2":
        usuario_a_borrar = input("Ingrese el nombre del usuario que desea eliminar: ").strip()
        usuario_encontrado = None
        for u in usuario.usuarios:
            if u["usuario"] == usuario_a_borrar:
                usuario_encontrado = u
                break

        # evita que se elimine al administrador principal
        if usuario_encontrado != None:
            if usuario_encontrado["usuario"] == "admin":
                print("\nALERTA")
                print("No puedes eliminar al administrador principal del sistema.")

            # elimina al usaurio de la lista de usuarios    
            else:
                usuario.usuarios.remove(usuario_encontrado)
                print("El usuario ha sido eliminado correctamente.")
        else:
            print("\nERROR")
            print("El usuario especificado no existe.")

    # abre el menu de inventario
    elif opcion_admin == "3":
        menu_inventario()

    # abre el modulo de ventas    
    elif opcion_admin == "4":
        print("Estas son las ventas")
        venta()

    #  muestra la lista de empleados registrados    
    elif opcion_admin == "5":
        print("\n" + "-" * 25)
        print("\nLista de empleados")
        print("\n" + "-" * 25)
        for u in usuario.usuarios:
            if u["rol"] == "empleado":
                print(u["usuario"])
        print("\n" + "-" * 25)
