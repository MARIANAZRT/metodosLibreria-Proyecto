def buscar_termino(termino, contenido):
    lineas = contenido.split("\n")
    encontradas = []

    for linea in lineas:
        if termino.lower() in linea.lower():
            encontradas.append(linea)

    return encontradas