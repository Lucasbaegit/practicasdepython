#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


facturas = {}


def sumaFacturas():
    print("Una vez iniciado el programa, tiene tres opcines T: terminar, A: agregar, C: cobrado.")
    agregar = ""
    cobrado = 0
    pendiente = 0
    while agregar != "T":
        if agregar == "A":
            numeroFactura = input("Introduzca el numero de factura: ")
            costeFactura = float(input("Introduzca el importe de la factura: "))
            facturas[numeroFactura] = costeFactura
            pendiente += costeFactura
        if agregar == "C":
            numeroFactura = input("Introduzca el numero de factura a cobrar: ")
            costeFactura = facturas.pop(numeroFactura, 0)
            pendiente -= costeFactura
            cobrado += costeFactura
        print("El monto cobrado es: ", cobrado)
        print("El monto pendiente de cobro es: ", pendiente)
        agregar = input("Intoduzca T: terminar, A: agregar, C: cobrado.")
        
sumaFacturas()
    