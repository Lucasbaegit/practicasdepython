#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def palabraInversa():
    palabra = input("Ingrese una palabra: ")
    cantidadDeLetras = len(palabra)
    posicion = cantidadDeLetras-1
    for i in range(cantidadDeLetras-1, -1, -1):
        
        letra = palabra[posicion]
        print(letra, end="\n")
        posicion -=1
    
palabraInversa()