from definiciones import registro_de_productos, menu_inventario
from ventas import venta
##base de datos de usuarios
usuarios=[["admin1","admin123","administrador"],
          ["kevin","12345","empleado"],
          ["alejandrina","12345","empleado"],
          ["adrian","12345","empleado"],
          ["ruddy","12345","empleado"],]

##variable para que el menu se mantenga visible hasta que se escoja salir
mantener=True

while mantener:
    print("Mercado MARKET")
    print("1.- iniciar sesion")
    print("2.- salir")
    opcion=input("Seleccione una opcion: ")

    if opcion=="1":
        ##para pedir usuario y contraseña
        ingresar_usuario=input("Ingrese su usuario: ")
        ingresar_contraseña=input("Ingrese su contraseña: ")

        ##variable que se mantendra en falso hasta que se encuentre un usuario y contraseña correcto
        login=False
        ##variable vacia  que se llenara con el rol del usuario registrado
        rol=""

        ##for para recorrer la lista de usuarios y verificar si el usuario y contraseña ingresados son correctos
        for usuario in usuarios:
            if ingresar_usuario==usuario[0] and ingresar_contraseña==usuario[1]:
                login=True
                rol=usuario[2]
                nombre_empleado=usuario[0]
                break

        if login:
            print("Bienvenid@", nombre_empleado) 
                
            if rol=="administrador":
                print("bienvenido", nombre_empleado)
                print("1.Registrar nuevo usuario")
                print("2.Registrar nuevo producto")
                print("3.ventas")
              
                opcion_admin=input("Seleccione una opcion: ")

                ##registro de nuevo empleado
                if opcion_admin=="1":
                    nuevo_usuario=input("ingrese nombre de nuevo empleado: ")
                    nueva_contraseña=input("ingrese contraseña de nuevo empleado: ")
                    ##usamos el append para añadir el nuevo usuario a la lista de usuarios
                    usuarios.append([nuevo_usuario, nueva_contraseña, "empleado"])

                    print("nuevo elemento añadido a las filas del gran Mercado MARKET")

                ##para mostrar la lista de empleados
                elif opcion_admin=="2":
                    #aqui pondremos registro de pro
                    menu_inventario()
                    for usuario in usuarios:
                        if usuario[2]=="empleado":
                            print(usuario[0])
                elif opcion_admin=="3":

                    print("estas son las ventas")
                    venta()

        else:
             print("datos erroneos, vuelva a intentarlo")

    elif opcion=="2":
         mantener=False
         print("gracias por su preferencia, vuelva pronto")
         print("Mercado MARKET siempre esta observando")                         