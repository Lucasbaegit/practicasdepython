#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

def carritoDeCompra():
    listaMasPrecio = {}
    siguienteItem = True
    while siguienteItem:
        articulo = input("Ingrese un articulo: ")
        precio = float(input("Ingrese el precio del articulo " + articulo + ": "))
        listaMasPrecio[articulo] = precio
        siguienteItem = input("Desea ingresar otro articulo SI/NO: ") == "SI"
    costo = 0
    for articulo, precio in listaMasPrecio.items():
        print(articulo, "\t", precio )
        costo += precio
    print("Costo total", costo)
        
carritoDeCompra()
    
    
        
    