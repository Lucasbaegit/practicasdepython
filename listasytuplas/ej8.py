#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def palindromo():
    palabra = input("Ingrese una palabra: ")
    listaDeLaPalabra = list(palabra)
    reversaListaDePalabra = reversed(palabra)
    reversaListaDePalabra = list(reversaListaDePalabra)
    
    
    
    if listaDeLaPalabra != reversaListaDePalabra:
            print("La palabra no es un palindromo")
    else:
            print("La palabra es un palindromo")
    
    
palindromo()