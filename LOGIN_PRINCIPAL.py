usuarios_registrados={}
name=(input("·····INGRESE EL NOMBRE DE SU MARKET··········"))
def registro():
    #regitro
    print("········BIENVENIDO AL SISTEMA MARKET······")
    name=(input("·····INGRESE EL NOMBRE DE SU TIENDA··········"))
    usu=(input("····INGRESE EL NOMBRE DEL USUARIO·········"))
    print("···BIENVENIDO",usu.upper())
    con=1
    while con<=3:
        print(f"......intento" ,con, "de 3")   
        contraseña=input(".......INGRESE UNA CONTRASEÑA DE 8 CARACTERES..........")
        b=(len(contraseña))
        if b>=8:
            print("contraseña correcta su cuenta fue guardada")
            usuarios_registrados[usu]=contraseña
            break
        else:
            print("contraseña insegura")
            con+=1
#incio_de_sesion
def inicio():
    print(".........INICIO DE SESIÓN DEL SISTEMA......")
    cont=1
    while cont<=3:
        t=input(".....INGRESE SU USUARIO.......")
        v=input(".........INGRESE SU CONTRASEÑA........")
        if t in usuarios_registrados and usuarios_registrados[t]==v:
            print("....INICIO DE SESIÓN CORRECTA,SEA BIENVENIDO",t.upper(),"A",name.upper())
            break
        else:
            print("...USUARIO O CONTRASEÑA INCORRECTA .....")
            cont+=1
#menu principal
while True:
    print(".......BIENVENIDO A MARKET........")
    print("......SELECCIONE UNA OPCION........")
    print("1.registro")
    print("2.inicio de sesion")
    print("3.salir")
    opc=int(input(".....ingrese una opcion......"))
    if opc==1:
        registro()
    elif opc==2:
        inicio()
        
    elif opc==3:
        print("saliendo del sistema muchas gracias por usar MARKET")
        break
    else:
        print("......opcion invalida.......")