#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def fecha():
    fecha_nacimiento=input("Ingrese su fecha de nacimiento con el formato dd/mm/aaaa: ")
    dia,mes,anio=fecha_nacimiento.split("/")
    dia=dia.zfill(2)
    mes=mes.zfill(2)
    print(f"La fecha de nacimiento es el dia {dia} mes {mes} y año {anio}")
    
fecha()
    