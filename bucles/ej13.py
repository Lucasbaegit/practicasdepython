#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def repeticion():
    frase = input("Ingrese una nueva palabra: ")
    while frase != "salir":
        print( "La palabra es incorrecta")
        frase = input("Ingrese una nueva palabra: ")
        
repeticion()
    