#las tuplas son un tipo de datos que nos permite crear una coleccion de datos para agruparlos
#no es necesario que los datos sean del mismo tipo

#en esta tupla se guardaran 4 tipos de datos
tupla = (1, 1.12, "hola", True)

#se pueden mostrar todos los valores juntos con print
print(tupla,"\n")
#se puede mostar un solo valor por medio de su "coordenada"
print(tupla[1], "\n") #recordar que python comienxa a contar desde el 0 en adelante por lo que aqui imprimiria el valor 1.12

#como tambien se pueden recorrer todos los valores uno por uno con 'for'
#con 'for' hay dos metodos para recorrer los valores

for valor in tupla:
    print(valor)
print("\n\n")
#metodo por cordenadas
for i in range(4):
    print(tupla[i])
print("\n\n")
for valor in tupla:
    print(f"{valor}, el valor es de tipo: {type(valor)}\n\n")

#lo que hay que tener en cuenta, es que las tuplas son inmutables por lo que
#NO SE PUEDEN MODIFICAR, AGREAR O ELIMINAR VALORES
#por ende lo siguiente daria error
#tupla[0] = "errorrr";

#lo que si se puede hacer es crear otra tupla juntando 2 tuplas
tuplaA = (1,2,3)
tuplaB = (4,5,6,6)
tuplaC = (tuplaA+tuplaB);
print(tuplaC)

#ademas tenemos algunas funciones utiles de python 
#contar la cantidad de veces que tiene un elemento dentro de una tupla con ".count()"
print(tuplaC.count(6))
#mostrar si existe un elemento dentro de la tupla
print(1 in tuplaC)#1 si se encuentra en la tupla C
print(8 in tuplaC)#8 no se encuentra en la tupla C