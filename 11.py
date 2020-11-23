vowels = ("a","e","i","o","u")
def contar_vocales(palabra):
    dic ={}.fromkeys(vowels,0)
    for c in palabra: 
        if c in dic: 
            dic[c] += 1  
    return dic


mi_frase = input("Ingrese una frase:")
lista_palabras = mi_frase.split()
diccionario_palabras = {}
for palabra in lista_palabras:
    if palabra not in diccionario_palabras:
        diccionario_palabras[palabra] = contar_vocales(palabra)
listado =[]
for p in diccionario_palabras:
    listado.append(f"{p} : {(diccionario_palabras[p])}")
for linea in listado:
    print(linea)
