def leer_archivo(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()

    if contenido.strip() == "":
        raise Exception("El archivo está vacío.")

    return contenido