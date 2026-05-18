def generar_resumen(contenido):
    lineas = contenido.split("\n")
    cantidad_lineas = len(lineas)
    palabras = len(contenido.split())

    return (
        "Resumen del contenido.\n"
        + "Cantidad de líneas: " + str(cantidad_lineas) + ".\n"
        + "Cantidad de palabras: " + str(palabras) + ".\n"
        + "Primeras líneas del texto:\n"
        + "\n".join(lineas[:3])
    )


def generar_relevante(contenido):
    lineas = [l for l in contenido.split("\n") if len(l.strip()) > 40]
    return "\n".join(lineas[:5]) or "No se encontraron líneas relevantes."