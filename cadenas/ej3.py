#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

def contar_letras():
    nombre=input("Ingrese su nombre: ")
    nombre_mayus=nombre.upper()
    print(nombre_mayus)
    contar_letras_del_nombre=len(nombre)
    print(contar_letras_del_nombre)
    
contar_letras()