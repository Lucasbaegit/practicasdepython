#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.



def resultado(n,m):

    c= n//m
    r= n%m
    return print(f" la division entre {n} y {m} da un cociente {c} y un resto {r}")
    
n= int(input("Ingrese un numero: "))
m= int(input("Ingrese un segundo numero: "))


resultado(n,m)








