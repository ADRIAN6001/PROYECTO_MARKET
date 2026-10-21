def registro():
    n=input("ingrese un numero")
    print(int(n)+int(n))
def inicio():
    nombre=input("ingrese un nombre")
    print(nombre)
while True:
    print(".........HOLA.........")
    print("1.registro")
    print("2.inicio")
    op= int(input("ingrese una opcion entre 1-2"))
    if op==1:
     registro()
    elif op==2:
     inicio()
     break
    else:
        print("opcion no valida")    
