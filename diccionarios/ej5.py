#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def mostrarCreditos():
    creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    
    sumaCreditos=0
    for materia, credito in creditos.items():
        print(f"La asignatura {materia} tiene {credito} creditos")
        sumaCreditos+=credito
        
    print(f"La cantidad de creditos totales es {sumaCreditos}")
    
    
mostrarCreditos()