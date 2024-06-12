#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.
num = int(input("Ingrese un numero: "));
nombre_archivo = f"tabla-{num}.txt";
with open(nombre_archivo, "w") as archivo:
        for i in range(1,11):
            archivo.write(f"{num} x {i} = {num*i}\n");
