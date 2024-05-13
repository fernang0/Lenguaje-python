edad = int(input("Ingrese su edad: "));
if edad>10 and edad<=18:
    print("El valor del ticket es $1000");
elif edad >18 and edad<=65:
    print("El valor del ticket es $2000");
elif edad>65:
    print("El valor del ticket es $1500");
else:
    print("El ticket es GRATISSS");
    
