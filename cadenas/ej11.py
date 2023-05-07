#Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


def productos():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    unidades = int(input("Ingrese el número de unidades: "))
    costo_total = precio_unitario * unidades

    print(f"{nombre_producto} {precio_unitario:8.2f} {unidades:03d} {costo_total:8.2f}")
    
productos()