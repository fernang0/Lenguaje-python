#Crear funciones

def sumar(x,y):
    return (x + y);

def area(x,y):
    return (x*y);
def perimetro(x,y):
    return (2*x+2*y);

x = int(input("Ingrese el primer numero: "));
y = int(input("Ingresa el segundo numero: "));

print("El area del rectangulo es: ", area(x,y));
print("El perimetro del rectangulo es: ", perimetro(x,y));