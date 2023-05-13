#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def loteria():
    listaDeNumero = []
    for i in range(6):
        numeroGanadoras = int(input("Ingrese los numeros ganadoras: " ))
        listaDeNumero.append(numeroGanadoras)
    
    listaDeNumero.sort()
    print(listaDeNumero)
    
    
loteria()