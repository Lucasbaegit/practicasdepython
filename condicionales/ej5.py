def grupos():
    a = input("Ingrese su sexto M o F: ")
    b = input("Ingrese su nombre: ")
    
    a = a[0]
    a = a.lower()
    b = b.lower()
    
    if (a == "f" and b < "m") or (a == "m" and b > "n"):
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")
        
grupos()