from archivo import leer_archivo
from gramatica import lenguaje_a_interpretar
from busqueda import ejecutar_busqueda
from resumen import generar_resumen, generar_relevante
from audio import los_resultados_pueden_ser_reproducidos_en_audio

COMANDOS = {
    "resumen": lambda p, c: generar_resumen(c),
    "relevante": lambda p, c: generar_relevante(c),
    "buscar": lambda p, c: ejecutar_busqueda(p, c),
    "audio": None
}

def iniciar():
    ruta = input("Archivo .txt: ").strip()
    try:
        contenido = leer_archivo(ruta)
    except Exception as e:
        print("Error:", e)
        return

    ultimo = ""
    while True:
        entrada = input(">>> ").strip()
        if entrada.lower() == "salir":
            break
        if not lenguaje_a_interpretar(entrada):
            print("Comando no reconocido.\n")
            continue
        partes = entrada.lower().split()
        if partes[0] == "audio":
            print((los_resultados_pueden_ser_reproducidos_en_audio(ultimo) if ultimo else "No hay resultado previo.") + "\n")
            continue
        ultimo = COMANDOS[partes[0]](partes, contenido)
        print(ultimo + "\n")

if __name__ == "__main__":
    iniciar()