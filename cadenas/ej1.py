#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


def imprimir_nombre():
    nombre=input("Ingrese su nombre: ")
    numero=int(input("Ingrese un numero entero: "))
    
    for i in range(numero):
        print(nombre)
        
        
imprimir_nombre()

    
    