#obteniendo numeros primos mediante el teorema de wilson

#primero definimos una funcion que nos de el factorial de un numero
def facto(x):
    a = 1;
    factorial=1;
    while a < x:
        a+=1;
        factorial*=a;
    return(factorial)
contador = 1;
while contador < 7:
    contador+=1;
    if ((facto(contador-1)+1)%contador) == 0:
        print(contador);
