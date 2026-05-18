from gtts import gTTS
import os


def los_resultados_pueden_ser_reproducidos_en_audio(texto_resultado):
    nombre_archivo = "resultado_audio.mp3"

    tts = gTTS(
        text=texto_resultado,
        lang="es",
        slow=False
    )

    tts.save(nombre_archivo)

    if os.path.exists(nombre_archivo):
        try:
            os.startfile(nombre_archivo)
        except:
            pass

    return "Se generó el archivo de audio: " + nombre_archivo