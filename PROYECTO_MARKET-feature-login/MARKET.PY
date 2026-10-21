#regitro
print("········BIENVENIDO AL SISTEMA MARKET······")
name_licor=(input("·····INGRESE EL NOMBRE DE SU TIENDA··········"))
usu=(input("····INGRESE EL NOMBRE DEL USUARIO·········"))
print("···BIENVENIDO",usu.upper())
con=1
while con<=3:
    print(f"......intento" ,con, "de 3")   
    contraseña=input(".......INGRESE UNA CONTRASEÑA..........")
    b=(len(contraseña))
    if b>=8:
        print("contraseña correcta su cuenta fue guardada")
        break
    else:
        print("contraseña insegura")
        con+=1
#LOGIN
print(".........INICIO DE SESIÓN DEL SISTEMA......")
cont=1
while con<=3:
    t=input(".....INGRESE SU USUARIO.......")
    v=input(".........INGRESE SU CONTRASEÑA........")
    if t==usu and v==contraseña:
        print("....INICIO DE SESIÓN CORRECTA,SEA BIENVENIDO",usu.strip(),"A",name_licor.upper())
        break
    else:
        print("...USUARIO O CONTRASEÑA INCORRECTA .....")
        cont+=1
