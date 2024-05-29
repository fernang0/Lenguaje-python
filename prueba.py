def validar(patente):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    numeros = "1234567890";
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
    patente = str(input("Ingresa una patente: "))
    print(validar(patente))