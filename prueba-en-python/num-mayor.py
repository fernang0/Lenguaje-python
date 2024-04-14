num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("Ingresa el segundo numero: "));
num3 = int(input("Ingresa el tercer numero: "));

if (num1>2 and num1>num3):
    print(num1, "es el numero mayor");
elif (num2>num1 and num2>num3):
    print(num2, "es el numero mayor");
elif (num3>num1 and num3>num1):
    print(num3, "es el numero mayor");
elif(num1==num2==num3):
    print("Son todos iguales");
else:
    print("Hay dos numeros iguales")
