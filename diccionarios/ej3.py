#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.



def direccionarioFrutas():
    frutas = {"Plátano":1.35, "Manzana":0.8, "Pera":0.85, "Naranja":0.7}
    ingresarFruta = input("Seleccione una fruta: ").title()
    kg = float(input("Ingrese una cantidad de kilos: "))
    
    if ingresarFruta in frutas:
        precio = frutas[ingresarFruta]*kg
        precioRedondeado = round(precio, 2)
        print(f"Para la cantidad de kilos {kg} de la fruta {ingresarFruta} el precio final es {precioRedondeado} " )
    else: 
        print("No disponemos de esa fruta")
        
direccionarioFrutas()