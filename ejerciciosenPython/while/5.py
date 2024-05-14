#obteniendo numeros primos mediante el teorema de wilson
#https://www.matematicas18.com/es/tutoriales/aritmetica/numero/numeros-primos/

#primero definimos una funcion que nos de el factorial de un numero
def facto(x):
    a = 1;
    factorial=1;
    while a < x:
        a+=1;
        factorial*=a;
    return(factorial)


contador = 0;
while contador < 100:
    contador+=1;
    if ((facto(contador-1)+1)%contador) == 0:
        print(contador);
