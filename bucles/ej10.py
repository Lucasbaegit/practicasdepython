#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def esPrimo():
    numero = int(input("Ingrese un numero mayor que 2: "))
    i=2
    while numero % i != 0:
            i+=1
    if i ==numero:
        print(f"el numero {numero} es primo")    
    else: 
        print(f"El numero {numero} no es primo")
        
esPrimo()
        
                
    