#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


def crearPersona():
    datosPersona = {}
    agregarDatos = True
    while agregarDatos == True:
        dato = input("Ingrese la categoria: ")
        valor = input(dato + ":")
        datosPersona[dato] = valor
        print(datosPersona)
        agregarDatos = input("Desea agregar mas datos: Si/No: ") == "Si"
        
 
    
crearPersona()



