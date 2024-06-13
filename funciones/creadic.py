from funciones import buscar;
dic={};
def creadic():
    key=input("Ingrese una key(SHAZAM para salir): ");
    if key.upper() == "SHAZAM":
        key = input("Ingrese la key que quiera saber el resultado: ");
        print(buscar(dic, key));
    else:
        value=input("Ingrese el valor de la key: ");
        dic[key]=value;
        creadic();
creadic();