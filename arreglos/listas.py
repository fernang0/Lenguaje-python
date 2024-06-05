#la diferencia de las listas con las tuplas es que se pueden: agregar, modificar y borrar elementos dentro de estas
#se pueden guardar distintos tipos de datos
#se utilizan los corchetes [] para las listas

lista = [1, 1.239, "m", False];
print(lista, "\n");

#con la funcion .append() podemos agregar elementos a una lista ya existente
lista.append("nuevo elemento");
print(lista, "\n");

#como en las tuplas tenemos 2 formas de listar sus elementos uno por uno
for elemento in lista:
    print(elemento);
print("\n\n")

#la funcion len() nos muestra la cantidad de elementos que tiene la lista
#se puede ocupar en string, para saber cuantas letras tiene una palabra por ejemplo
for i in range(len(lista)):
    print(lista[i])
print("\n\n")
#remplazaremos el elemento numero 2 de la lista
lista[2] = 123882
#ahora el elemento 'm' es 123882
print(lista)
print("\n\n")

#como en las tuplas podemos juntar dos listas
listaA = [1,2,3];
listaB = [4,5,6];
listaC = listaA+listaB;
print(listaC);
print("\n\n")
# ++++Probar listaA.append(listaB) +++++
