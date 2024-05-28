nombres = [];

while True:
    nombre = str(input("Ingrese un nombre: "));
    nombres.append(nombre);
    pregunta = (str(input("Quiere agregar otro nombre?(si/no): "))).lower();
    if pregunta == "no":
        break;
for n in nombres:
    if len
