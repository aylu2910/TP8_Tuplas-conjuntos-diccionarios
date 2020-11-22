def son_ortogonales(v1,v2):
    return "Son ortogonales" if v1[0]*v2[0] + v1[1]*v2[1] ==0 else "No son ortogonales"



a1 = int(input("Ingrese un numero para el vector A:"))
a2 = int(input("Ingrese un numero para el vector A:"))
b1 = int(input("Ingrese un numero para el vector B:")) 
b2 = int(input("Ingrese un numero para el vector B:")) 
vector_1 = (a1,a2) 
vector_2 = (b1,b2)
print(son_ortogonales(vector_1,vector_2))