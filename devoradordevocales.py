palabra = str(input("Ingresa una palabra: "));
palabra = palabra.upper();
for letra in palabra:
    if letra in "AEIOU":
        continue;
    else:print(letra);
