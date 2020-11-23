def incrementar_precios(dic):
    for p in dic:
        dic[p] += dic[p]*0.15
    return dic
inicio = int(input("Presione 1 para continuar:"))
dic ={}
while inicio == 1:    
    producto = input("Ingrese producto: ")
    precio = int(input("Ingrese precio: "))    
    if producto not in dic:
        dic[producto] = precio
    inicio = int(input("Presione 1 para continuar o 0 para finalizar:"))
    
incrementado = incrementar_precios(dic)
for i in incrementado:
    print(f"Producto:{i} - ${incrementado[i]}")
    

    