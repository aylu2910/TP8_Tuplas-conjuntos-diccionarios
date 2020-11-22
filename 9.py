def tabla_de_multiplicar(n):
    return {x:x*n for x in range(1,13)}

num = int(input("Ingrese un numero para saber su tabla de multiplicar:"))
print(tabla_de_multiplicar(num))