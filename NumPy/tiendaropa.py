import numpy as np
#Escribe un programa en Python que solicite al usuario la cantidad de cada tipo de prenda en cada talla y luego calcule el costo total de la compra.
precios = np.array([[10,12,15], [20,25,30],[35,40,45]]);
carrito = np.zeros((3,3));
prendas = ["Camiseta", "Pantalon", "Chaqueta"];
tallas = ["Small", "Medium", "Large"];
def mostrar_precios():
    x = 0;
    y = 0;
    for prenda in prendas:
        for talla in tallas:
            print(prenda, talla, "=", "$",precios[x][y]);
            y+=1;
        x+=1;y=0;
def mostrar_tallas():
    print("""
Que talla:
1)Small
2)Medium
3)Large
0)Menu principal
    """);
def camisetas():
    mostrar_tallas();
    opcion = int(input("Que talla desea comprar: "));
    match opcion:
        case 1:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[0,0] = cantidad;
            camisetas();
        case 2:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[0,1] = cantidad;
            camisetas();
        case 3:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[0,2] = cantidad;
            camisetas();
        case 0:
            comprar();

def pantalones():
    mostrar_tallas();
    opcion = int(input("Que talla desea comprar: "));
    match opcion:
        case 1:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[1,0] = cantidad;
            camisetas();
        case 2:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[1,1] = cantidad;
            camisetas();
        case 3:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[1,2] = cantidad;
            camisetas();
        case 0:
            comprar();
def chaquetas():
    mostrar_tallas();
    opcion = int(input("Que talla desea comprar: "));
    match opcion:
        case 1:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[2,0] = cantidad;
            camisetas();
        case 2:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[2,1] = cantidad;
            camisetas();
        case 3:
            cantidad = int(input("Ingrese la cantidad: "));
            carrito[2,2] = cantidad;
            camisetas();
        case 0:
            comprar();
def total():
    return (np.sum(carrito*precios))
def comprar():
    print("""
1) Camisetas
2) Pantalones
3) Chaquetas
0) Mostrar total de mi carrito
""");
    opcion = int(input("Que desea comprar: "));
    match opcion:
        case 1:
            camisetas();
        case 2:
            pantalones();
        case 3:
            chaquetas();
        case 0:
            print("El total de su compra es de: ", total());
mostrar_precios();
comprar();
