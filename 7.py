conj = set(range(10))
n = int(input("Ingrese un numero a eliminar:"))
while n!=-1:
    try:
        conj.remove(n)
        print(conj)
        n = int(input("Ingrese un numero a eliminar:"))
    except KeyError:
        print("El numero no se encuentra,intente nuevamente")
        n = int(input("Ingrese un numero a eliminar:"))
    