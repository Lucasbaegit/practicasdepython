#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

def piramide():
    numero = int(input("Ingrese un numero entero: "))
    for i in range(1, numero+1):
        
        print("*" * i)
        
        
piramide()