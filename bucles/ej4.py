#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def cuentaRegresiva():
    numero= int(input("Ingrese un numero entero positivo: "))
    for i in range(numero):
        print(numero, end=", ")
        numero-=1

cuentaRegresiva()