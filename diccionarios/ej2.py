#Escribir un programa que pregunte al persona su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.



def getPersona():
    nombre = input("Como te llamas: ")
    edad = input("Cual es tu edad: ")
    direccion = input("Cual es tu direccion: ")
    telefono = input("Cual es tu numero de telefono: ")
    persona = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono }
    print(persona)
  
    print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su número de teléfono es {persona['telefono']}.")
    
getPersona()
    

