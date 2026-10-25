from DEFINICIONES import registro_de_productos, menu_inventario
from ventas import venta
##base de datos de usuarios
usuarios=[ {"usuario": "admin", "contraseña": "admin123", "rol": "administrador"},
           {"usuario": "kevin", "contraseña": "12345", "rol": "empleado"},
           {"usuario": "alejandrina", "contraseña": "12345", "rol": "empleado"},
           {"usuario": "adrian", "contraseña": "12345", "rol": "empleado"},
           {"usuario": "ruddy", "contraseña": "12345", "rol": "empleado"}]

##variable para que el menu se mantenga visible hasta que se escoja salir
mantener=True

while mantener:
    print("\n Mercado MARKET")
    print("1.- iniciar sesion")
    print("2.- salir")
    opcion=input("Seleccione una opcion: ").strip()

    if opcion=="1":
        ##para pedir usuario y contraseña
        ingresar_usuario=input("Ingrese su usuario: ").strip()
        ingresar_contraseña=input("Ingrese su contraseña: ")

        ##variable que se mantendra en falso hasta que se encuentre un usuario y contraseña correcto
        login=False
        ##variable vacia  que se llenara con el rol del usuario registrado
        rol=""
        nombre_empleado=""

        ##for para recorrer la lista de usuarios y verificar si el usuario y contraseña ingresados son correctos
        for u in usuarios:
            if ingresar_usuario == u["usuario"] and ingresar_contraseña == u["contraseña"]:
                login = True
                rol = u["rol"]
                nombre_empleado = u["usuario"]
                break

        if login:
            print("Bienvenid@", nombre_empleado) 
                
            if rol=="administrador":
                print("\n Menu del administrador")
                print("1.Registrar nuevo empleado")
                print("2.registro de inventario")
                print("3.ventas")
                print("4.mostrar lista de empleados")
              
                opcion_admin=input("Seleccione una opcion: ").strip()

                ##registro de nuevo empleado
                if opcion_admin=="1":
                    nuevo_usuario=input("ingrese nombre de nuevo empleado: ").strip()
                    ## en caso de que el usuario ingrese un numero
                    contiene_numero=False
                    for letra in nuevo_usuario:
                        if letra.isdigit():
                            contiene_numero=True

                    if contiene_numero:
                        print("\nALERTA DE ERROR")
                        print("el nombre de usauio no puede contener numeros")
                    else:
                        nueva_contraseña=input("ingrese contraseña de nuevo empleado: ")

                        ##creamos el nuevo usuario en una lista de diccionario
                        nuevo_empleado_añadido={"usuario":nuevo_usuario,"contraseña":nueva_contraseña,"rol":"empleado"}
                        ##ahora lo añadimos a la lista de usuarios
                        usuarios.append(nuevo_empleado_añadido)
                        print("nuevo elemento añadido a las filas del gran Mercado MARKET")

                ##para mostrar la lista de empleados
                elif opcion_admin=="2":
                    #aqui pondremos registro de pro
                    menu_inventario()
                
                elif opcion_admin=="3":
                    print("estas son las ventas")
                    venta()

                elif opcion_admin=="4":
                    print("\nLista de empleados")
                    for u in usuarios:
                        if u["rol"]=="empleado":
                            print(u["usuario"])

        else:
             print("datos erroneos, vuelva a intentarlo")

    elif opcion=="2":
         mantener=False
         print("gracias por su preferencia, vuelva pronto")
         print("Mercado MARKET siempre esta observando")                         