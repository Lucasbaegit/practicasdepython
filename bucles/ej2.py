#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def edad():
    edad = int(input("Escriba su edad: "))
    a=0
    for i in range(1, edad+1):
        print(i)
        i+=1
        
edad()
        
    