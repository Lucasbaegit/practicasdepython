#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def cambiarFormato():
    meses = {1 : "Enero", 2 : "Febrero",  3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    fecha = input("Ingrese una fecha en el siguiente formato dd/mm/aaaa")
    fecha = fecha.split("/")
    print(f"{fecha[0]} de {meses[int(fecha[1])]} y el año {fecha[2]}")
    
    
    
    
cambiarFormato()

