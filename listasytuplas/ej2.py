#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

def lista():
    listaUno = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    numero = 0
    for numero in range(len(listaUno)):
        asignatura = listaUno[numero]    
        print(f"Yo estudio la asignatura {asignatura}")
        numero +=1
        
lista()
            
        
    
    