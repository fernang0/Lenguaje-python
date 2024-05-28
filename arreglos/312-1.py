nombre = [];
larger = "";
for i in range(3):
    n = str(input("Ingrese un nombre: "));
    if len(n) > len(larger):
        larger = n;
    nombre.append(n);

print("el nombre mas largo es: ",larger);
