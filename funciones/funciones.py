def buscar(dicc, key):
    if key in dicc: return dicc[key]
    else: return f"La key: {key} no se encuentra en el diccionario: {dicc}";