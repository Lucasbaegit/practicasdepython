#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def monedas():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    consulta = input("Escriba una moneda: ")
    print(divisas.get(consulta.title(), "La moneda no esta enlistada"))
    
monedas()
    
    


