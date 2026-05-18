def lenguaje_a_interpretar(cadena):
    partes = cadena.lower().split()

    if len(partes) == 1:
        if partes[0] in ["resumen", "relevante", "audio"]:
            return True

    if len(partes) == 2:
        if partes[0] == "buscar":
            return True

    if len(partes) == 4:
        if partes[0] == "buscar" and partes[2] in ["y", "o"]:
            return True

    return False