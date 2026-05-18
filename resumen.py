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