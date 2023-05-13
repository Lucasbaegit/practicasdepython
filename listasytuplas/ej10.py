#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

def listaDePrecios():
    precio = [50, 75, 46, 22, 80, 65, 8]
    precio.sort()
    
    menorPrecio = precio[0]
    mayorPrecio = precio[-1]
    
    print(f"El menor precio es {menorPrecio} y el mayor {mayorPrecio} ")
    
    
listaDePrecios()