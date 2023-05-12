#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "abc123"

def seguro():
    claveUsuario = input("Ingrese su contraseña: ")
    while contraseña != claveUsuario:
        claveUsuario = input("Ingrese su contraseña: ")
        
seguro()
        