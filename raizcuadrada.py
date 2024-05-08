#para obtener la raiz de un numero no es necesario importar ningun modulo
#una raiz en matematicas es una potencia, pero potencia fraccionaria
#la raiz cuadrada de 4 se puede escribir de la siguiente manera 4**(1/2) y la raiz cubica de 9 se puede escribir de la siguiente manera 9**(1/3) por lo que
#Simplemente seria una potencia de exponente fraccionario a elevado a m dividido en n a**(m/n) = raiz
#n debe ser diferente a 1
def raiz(a,m,n):
    return a**(m/n)
a = int(input("Ingrese la cantidad subradical: "));
m = int(input("Ingrese el exponente del subradical: "));
n = int(input("Ingrese el indice: "))
print(raiz(a,m,n));
