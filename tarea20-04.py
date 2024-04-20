def contarvocales(palabra):
    contador = 0;
    for letra in palabra:
        if letra.lower() in 'aeiou':
            contador+=1;
    return contador;
def contadordeletras(palabra):
    contador = 0;
    for letra in palabra:
        contador += 1;
    return contador;
def contarpalabras(palabra):
    contador = 1;
    for letra in palabra:
        if letra == " ":
            contador += 1;
    return contador;

print(contarpalabras("Hola mundo aeiou"))
