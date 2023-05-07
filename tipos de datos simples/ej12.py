#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


def coste_final(cantidad_de_barras_de_ayer):
    precio_habitual = 3.49
    descuento = 60
    descuento_aplicable = descuento/100+1
    precio_con_descuento = precio_habitual/descuento_aplicable
    total_dia_de_ayer= cantidad_de_barras_de_ayer*precio_con_descuento
    return print(f"El precio habitual de una barra de pan es ${precio_habitual}, por una barra del dia anterior se le hace un descuento de {descuento}% y el costo total vendido de barras no frescas es de ${total_dia_de_ayer} ")
    

cantidad_de_barras_de_ayer= int(input("Ingrese la cantidad de barras que no son frescas vendidas: "))

coste_final(cantidad_de_barras_de_ayer)
