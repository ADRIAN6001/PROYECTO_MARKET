import usuario
import administrador

## para mantener el programa en ejecucion
mantener = True

while mantener:
    print("\n" + "=" * 30)
    print("\n Mercado MARKET")
    print("\n" + "=" * 30)

    print("1.- iniciar sesion")
    print("2.- salir")
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        ingresar_usuario = input("Ingrese su usuario: ").strip()
        ingresar_contraseña = input("Ingrese su contraseña: ")

        ## para validar el usuario y contraseña
        login, rol, nombre_empleado = usuario.autenticar_usuario(ingresar_usuario, ingresar_contraseña)

        if login:
            print("Bienvenid@ ", nombre_empleado) 

            ## ingresa al menu de administrador    
            if rol == "administrador":
                administrador.ejecutar_menu_admin()

            ## ingresa al menu de empleado    
            elif rol == "empleado":
                usuario.ejecutar_menu_empleado()
        else:
             print("Datos erroneos, vuelva a intentarlo")

    elif opcion == "2":
         
         ## cierra el bucle y termina el programa
         mantener = False
         print("\n" + "=" * 45)
         print("Gracias por su preferencia, vuelva pronto")
         print("Mercado MARKET siempre esta observando")                         
         print("\n" + "=" * 45)
