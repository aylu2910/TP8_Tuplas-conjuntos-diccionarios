frase = input("Ingrese una frase:")
conj = frase.split()
conj.sort(key=len)
sin_repeticiones = set(conj)
print(conj,sin_repeticiones)