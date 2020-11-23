#SOLUCION CON TUPLAS
def domino(f1,f2):
    if f1[0] in f2 or f1[1] in f2:
        return True
    else:
        return False
    
n1 = int(input("Ingrese un numero para completar la ficha 1:"))
n2 = int(input("Ingrese un numero para completar la ficha 1:"))
n3 = int(input("Ingrese un numero para completar la ficha 2:"))
n4 = int(input("Ingrese un numero para completar la ficha 2:"))
ficha_1 = {n1,n2}
ficha_2 = {n3,n4}
print(ficha_1,ficha_2)
print(domino(ficha_1,ficha_2))

#SOLUCION CON CONJUNTOS SET() => Uso la intersección

def domino(f1,f2):
    return f1&f2
    
n1 = int(input("Ingrese un numero para completar la ficha 1:"))
n2 = int(input("Ingrese un numero para completar la ficha 1:"))
n3 = int(input("Ingrese un numero para completar la ficha 2:"))
n4 = int(input("Ingrese un numero para completar la ficha 2:"))
ficha_1 = {n1,n2}
ficha_2 = {n3,n4}
print(ficha_1,ficha_2)
print(domino(ficha_1,ficha_2))