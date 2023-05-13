#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

def vocales():
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower()
    palabra = list(palabra)
    
    contadorDeA = 0
    contadorDeE = 0
    contadorDeI = 0
    contadorDeO = 0
    contadorDeU = 0
    for i in range(len(palabra)):
        if palabra[i] == "a":
            contadorDeA +=1
    for i in range(len(palabra)):
        if palabra[i] == "e":
            contadorDeE +=1
    for i in range(len(palabra)):
        if palabra[i] == "i":
            contadorDeI +=1
    for i in range(len(palabra)):
        if palabra[i] == "o":
            contadorDeO +=1
    for i in range(len(palabra)):
        if palabra[i] == "u":
            contadorDeU +=1            
    
    print(f"Las letras aparecen: ´a´ = {contadorDeA}, ´e´ = {contadorDeE}, ´i´ = {contadorDeI}, ´o´ = {contadorDeO} y ´u´ = {contadorDeU}")
    
vocales()