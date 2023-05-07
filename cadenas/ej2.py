#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

def escribir_nombre():
    nombre= input("Ingrese su nombre: ")
    nombre_minuscula= nombre.lower()
    print(nombre_minuscula)
    nombre_mayuscula= nombre.upper()
    print(nombre_mayuscula)
    nombre_letra_capital=nombre.title()
    print(nombre_letra_capital)
    
escribir_nombre()