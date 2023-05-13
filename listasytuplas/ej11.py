#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def productoEscalar():
    vector1 = [1,2,3]
    vector2 = [-1,0,2]
    productoDeVectores = []
    for i in range(len(vector1)):
        
        resultado = vector1[i] * vector2[i]
        
        productoDeVectores.append(resultado)
    resultadoFinal = productoDeVectores[0] + productoDeVectores[1] + productoDeVectores[2]
    print(f"El producto del escalar {str(vector1)} y el escalar {str(vector2)} es {resultadoFinal}")
        
productoEscalar()
        
    