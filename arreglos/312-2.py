nombre = [];
apellidos = [];

for i in range(3):
    nom = str(input("Ingrese un nombre: "));
    ape = str(input("Ingrese el apellido: "));
    nombre.append(nom);apellidos.append(ape);

for n in range(3):
    print(nombre[n], apellidos[n]);
