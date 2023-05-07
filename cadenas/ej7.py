#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def reemplazar_dominio():
    mail=input("Ingrese un mail: ")
    separacion_mail= mail.split("@")
    nuevo_mail=separacion_mail[0]+"@ceu.es"
    print(nuevo_mail)
    
reemplazar_dominio()
    