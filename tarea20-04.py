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
    if palabra == True:
        contador = 1;
        for letra in palabra:
            if letra == " ":
                contador += 1;
        return contador;
    else:return 0;

print(contarpalabras(""))
