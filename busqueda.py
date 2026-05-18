def buscar_termino(termino, contenido):
    lineas = contenido.split("\n")
    return [linea for linea in lineas if termino.lower() in linea.lower()]


def ejecutar_busqueda(partes, contenido):
    res1 = buscar_termino(partes[1], contenido)
    if len(partes) == 2:
        return "\n".join(res1) or "Sin resultados para: " + partes[1]
    res2 = buscar_termino(partes[3], contenido)
    combinados = [l for l in res1 if l in res2] if partes[2] == "y" else list(dict.fromkeys(res1 + res2))
    return "\n".join(combinados) or "Sin resultados."