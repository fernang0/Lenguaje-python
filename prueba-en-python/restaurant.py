def menu_principal():
    print('''
1. Ingresar nombre del cliente
2. Menu de platos juntos con sus precios
3. Total boleta
4. Salir
''')
def menu_platos():
    print('''
    
1. Arroz a la francesa – $4.500
2. Arroz marinero – $5.200
3. Sopa marinera –$9.700
4. Menu principal
''')
boleta = 0;
menu_principal();
opcion = int(input("Ingrese una opcion: "))
while True:
    match opcion:
        case 1:
            nombre_cliente = str(input("Ingrese el nombre del cliente: "));
            menu_principal();
            opcion = int(input("Ingrese una opcion: "));
        case 2:
            menu_platos();
            opcion_plato = int(input("Que plato desea elegir: "));
            match opcion_plato:
                case 1:
                    boleta += 4500;
                case 2:
                    boleta += 5200;
                case 3:
                    boleta += 9700;
                case 4:
                    menu_principal();
                    opcion = int(input("Ingrese una opcion: "));
        case 3:
            print("El total de la boleta es $", boleta);
            break;
        case 4:
            print("Adios ",nombre_cliente,", el valor de la boleta es: $", boleta);
            break;
        case _:
            print("No es una opcion disponible");
            menu_principal();
            opcion = int(input("Ingrese una opcion: "));
