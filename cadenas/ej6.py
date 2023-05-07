#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def mayus_vocal():
    frase=input("Ingrese una frase: ")
    vocal=input("Ingrese la vocal que quiere que se vea en mayuscula: ")
    frase_minus=frase.lower()
    vocal_minus=vocal.lower()
    vocal_mayus=vocal.upper()
    
    frase_con_vocal_mayus= frase_minus.replace(vocal_minus,vocal_mayus)
    print(frase_con_vocal_mayus)
    
mayus_vocal()
    