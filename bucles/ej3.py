#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numerosImpar():
    numeroEntero = int(input("Escriba un numero entero positivo: "))
    if numeroEntero%2 ==0:
        for i in range(1, numeroEntero+1): 
            if i%2 !=0:
                print(i, end=", ")
    else:
        print("El numero ingresado no es un numero par positivo, ingrese otro numero: ")
        
                
                
numerosImpar()