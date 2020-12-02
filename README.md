# TP8_Tuplas-conjuntos-diccionarios
## EJ 1
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa para verificar su comportamiento:
a.Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida. 
b.Sumar N días a una fecha. 
c.Ingresar un horario desde teclado, verificando que sea correcto. 
d.Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerará que el primero corresponde al día anterior. En ningún caso la diferencia en horas puede superar las 24 horas.
## EJ 2
Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de 2017". Escribir también un programa para verificar su comportamiento.
## EJ 3
Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una dirección de correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección. Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar)
## EJ 4
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True o False. Escribir también un programa para verificar su comportamiento.
## EJ 5
En geometría un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. Los vectores en el plano se representan mediante un par orde- nado de números reales (x, y) llamados componentes. 
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo,basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
## EJ 6
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
## EJ 7
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove, mostrando el con- tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.
## EJ 8
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
## EJ 9
Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar la función.
## EJ 10
Desarrollar una función eliminarclaves() que reciba como parámetros un dicciona- rio y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento
## EJ 11
Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a la función por cada palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales hallada
## EJ 12
Una librería almacena su lista de precios en un diccionario. Diseñar un programa para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cuál es el ítem más costoso que venden en el comercio.
## EJ 13
Escribir una función buscarclave() que reciba como parámetros un diccionario y un valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado
