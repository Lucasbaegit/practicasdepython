#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

def asignacionDeNotas():
    listaUno = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    notas = []
    numero = 0
    for numero in range(len(listaUno)):
        asignatura = listaUno[numero]
        relacionDeNotas = int(input(f"Que te has sacado en la asinatura {asignatura}: "))
        notas.append(relacionDeNotas)
        numero+=1
    for numero in range(len(listaUno)):
        asignatura = listaUno[numero]
        notasPorAsignatura = notas[numero]
        print(f"En la asignatura {asignatura} la nota del alumano fue {notasPorAsignatura}") 
        numero+=1
    
asignacionDeNotas()