#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def contarLetra():
    frase = input("Escriba una frase: ")
    letra = input("Escriba una letra que quiere que cuente: ")
    
    cantidadDeLetras = len(frase)
    contador = 0
    
    for i in range (cantidadDeLetras-1):
        coincide = frase[i]
        if letra == coincide:
            contador +=1
        
    print(f"La cantidad de veces que aparece la letra {letra} es {contador}")
        
    
contarLetra()