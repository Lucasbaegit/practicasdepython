#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

def lista():
    listaHasta10 = []
    
    for i in range(1, 11):
        numero = i
        listaHasta10.append(numero)
        
    for i in range(0, 10):    
        print(listaHasta10[i], end=",")
        
    
lista()
        
    