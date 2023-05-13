#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def asignacionDeNotas():
    listaUno = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    notas = []
    numero = 0
    for numero in range(len(listaUno)):
        asignatura = listaUno[numero]
        relacionDeNotas = int(input(f"Que te has sacado en la asinatura {asignatura}: "))
        notas.append(relacionDeNotas)
        numero+=1
       
    for i in range(0, len(notas)):    
        if notas[i] < 6:
            print(f"La asignatura {listaUno[i]} debe repetirse")
            
asignacionDeNotas()
            