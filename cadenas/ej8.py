#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def dos_decimales():
    precio=round(float(input("Ingrese el precio con dos decimales: ")),2)
    precio_texto=str(precio)
    separacio_de_precio=precio_texto.split(".")
    parte_entera=separacio_de_precio[0]
    parte_decimal=separacio_de_precio[1]
    print(f"El precio es {parte_entera} con {parte_decimal}")
    
dos_decimales()
