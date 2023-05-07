#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

def capital_obtenido(cantidad, interes, años):
    interesb= interes/100+1
    capital_final= cantidad*interesb*años
    
    return print(f" La cantidad obtenida con {cantidad} teniendo un intereses de {interes} y una cantidad de años {años} es {capital_final}")

cantidad=float(input("Ingrese un monto: "))
interes=float(input("Ingrese el interes: "))
años=float(input("Ingrese la cantidad de años: "))

capital_obtenido(cantidad,interes,años)




