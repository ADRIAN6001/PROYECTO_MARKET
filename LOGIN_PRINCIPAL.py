##base de datos de usuarios
usuarios=[["admin1","admin123","admin"],
          ["kevin","12345","usuario"],
          ["alejandrina","12345","usuario"],
          ["adrian","12345","usuario"],
          ["ruddy","12345","usuario"],]

##para pedir usuario y contraseña
ingresar_usuario=input("Ingrese su usuario: ")
ingresar_contraseña=input("Ingrese su contraseña: ")

login=False

##for para recorrer la lista de usuarios y verificar si el usuario y contraseña ingresados son correctos
for usuario in usuarios:
    if ingresar_usuario==usuario[0] and ingresar_contraseña==usuario[1]:
        login=True
        print("Bienvenido", usuario[0])
        break

if login==False:
    print("Usuario o contraseña incorrectos")