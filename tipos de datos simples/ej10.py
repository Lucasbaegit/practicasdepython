#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


def peso_total(cantidad_de_payasos, cantidad_de_muñecas):
    peso_del_pedido= (cantidad_de_payasos*112 + cantidad_de_muñecas*75)/1000
    
    return print(f"Con una cantidad de payasos {cantidad_de_payasos} y una cantidad de muñecas {cantidad_de_muñecas} el peso en kilos del pedido es de {peso_del_pedido}")
    
    
    
cantidad_de_payasos= int(input("Ingrese la cantidad de payasos: "))
cantidad_de_muñecas= int(input("Ingrese la cantidad de muñecas: "))

peso_total(cantidad_de_payasos, cantidad_de_muñecas)

    