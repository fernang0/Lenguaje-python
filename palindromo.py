
def palindromo(txt: str):
    txt = txt.replace(' ', '').lower()
    return txt == txt[::-1]

texto1 = "Sé verlas al revés"
print(palindromo(texto1))
