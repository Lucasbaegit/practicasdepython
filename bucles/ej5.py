#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def interes():
    monto = int(input("Ingrese el monto a invertir: "))
    interes = int(input("Ingrese el interes en porcentaje: "))
    interes = interes/100+1
    años = int(input("Ingrese la cantidad de años: "))
    cadaAño = monto
    for i in range(1, años+1):
        cadaAño = cadaAño*interes
        cadaAño = round(cadaAño, 2)
        print(f"El monto final en el año {i} es: {cadaAño}")
        
interes()