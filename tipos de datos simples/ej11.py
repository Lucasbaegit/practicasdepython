#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def saldo_por_año(monto):
    año1=round(monto*1.04,2)
    año2=round(año1*1.04,2)
    año3=round(año2*1.04,2)
    
    return print(f"Con el monto {monto} al año 1 se puede retirar {año1}, al año 2 {año2} y al año 3 {año3}")
    
    
monto = float(input("Ingrese el monto del año 0: "))

saldo_por_año(monto)