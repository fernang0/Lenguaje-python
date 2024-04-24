def contarvocales(palabra):
    contador = 0;
    for letra in palabra:
        if letra.lower() in 'aeiou':
            contador+=1;
    return contador;

def contarletras(palabra):
    contador = 0;
    for letra in palabra:
        contador += 1;
    return contador;

def contarpalabras(palabra):
    contador = 0;
    for letra in palabra:
        if letra == " ":
            contador += 1;
    return contador;
def contapalabras(palabras):
    dentro = 1;
    fuera = 0;
    estado = fuera;
    contador = 0;
    for letra in palabras:
        if letra != " ":
            estado = dentro;
        elif letra == " ":
            contador += 1;
            estado = fuera;
    if estado == dentro:
        return contador+1;
print("""
1) Contar vocales
2) Contar letras
3) Contar palabras
""");
opcion = int(input("Ingrese una opcion: "));
match opcion:
    case 1:
