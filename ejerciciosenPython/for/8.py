#factorial de 5 = 5 * 4 * 3 * 2 *1

factorial = 1;
num = int(input("Ingrese un numero para saber su factorial: "));
for i in range(1,num+1):
    factorial*=i;

print(factorial);
