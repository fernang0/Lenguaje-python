vehiculos = [[],[],[],[]];

<<<<<<< HEAD
def validar(patente):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    numeros = "1234567890";
=======
def formato(patente):
    #esta funcion se puede mejorar
<<<<<<< HEAD
=======
>>>>>>> f4d876e (ordenando y desechando)
>>>>>>> refs/remotes/origin/master
    if len(patente) == 6:
        if patente[0] in caracteres and patente[1] in caracteres:
            if patente[2] in caracteres and patente[3] in caracteres:
                if patente[4] in numeros and patente[5] in numeros:
                    return True;
                else:
                    return False;
            elif patente[2] in numeros and patente[3] in numeros:
                if patente[4] in numeros and patente[5] in numeros:
                    return True;
                else:
                    return False;
            else:
                return False;
        else:
            return False;
    else:
        return False;


while True:
    print("""
Bienvenido al Parking VIP
¿que desea hacer?
1.- Ingresar un vehículo
2.- Listar vehículos
3.- Borrar un vehículo
4.- Conteo de vehículos
5.- Salir
""");
    opcion = int(input("Ingresa una opcion: "));
    match opcion:
        case 1:
            piso = int(input("Ingrese el piso en el cual quiere ingresar el vehiculo(1-4): "));
            patente = (str(input("Ingrese la patente: "))).upper();
            while validar(patente) == False:
                patente = (str(input("Ingrese la patente correcta, debe tener 6 digitos(AABB99-AA8899): "))).upper();
            vehiculos[piso-1].append(patente);
            print(vehiculos);
        case 2:
            print("""
1.- Listar todos
2.- Listar un piso específico
3.- Volver
""");
            listar = int(input("Ingrese una opcion: "));
            match listar:
                case 1:
                    print(vehiculos);
                case 2:
                    piso = int(input("Que piso quiere listar(1-4): "));
                    print(vehiculos[piso-1]);
                case 3:
                    continue;
        case 3:
            borrar = (str(input(("Ingrese el vehículo a borrar: ")))).upper();
            for n in range(0,4):
                if borrar in vehiculos[n]:
                    vehiculos[n].remove(borrar);
        case 4:
            print("""
1.- Mostar cantidad de vehículos en total
2.- Mostar cantidad de vehículos por piso
3.- Mostar cantidad de vehículos de un piso
4.- Volver
""");
            opcion = int(input("Ingrese una opcion: "));
            match opcion:
                case 1:
                    total = 0;
                    for i in range(4):
                        total += len(vehiculos[i])
                    print(total)
                case 2:
                    for i in range(4):
                        print(f"Piso {i+1} = {len(vehiculos[i])} vehiculos")

                    continue;
                case 3:
                    piso = int(input("Ingrese el piso(1-4): "))
                    print(len(vehiculos[piso]))
                    continue;
                case 4:
                    continue;
        case 5:
            print("Adios");
            break;
        case _:
            print("Esta no es una opcion valida");
