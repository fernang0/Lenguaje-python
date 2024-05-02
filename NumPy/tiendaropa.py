import numpy as np
#Escribe un programa en Python que solicite al usuario la cantidad de cada tipo de prenda en cada talla y luego calcule el costo total de la compra.
precios = np.array([[10,12,15], [20,25,30],[35,40,45]]);
def mostrar_precios():
    prendas = ["Camiseta", "Pantalon", "Caqueta"];
    tallas = ["Small", "Medium", "Large"]
    x = 0;
    y = 0;
    for prenda in prendas:
        for talla in tallas:
            print(prenda, talla, "=", "$",precios[x][y])
            y+=1;
        x+=1;y=0;
mostrar_precios()
