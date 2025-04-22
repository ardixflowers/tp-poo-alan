import os
from persona import *
from ingeniero import *
from director import *
from astronauta import *

if __name__ == "__main__":
    try:
        astronauta = Astronauta("Franco Colapinto", "78456126", "Argentina")
        ingeniero = Ingeniero("Gaetan Jego", "12345678", "Ingles")
        director = Director("James Vowles", "12345678", "Britanico")

        director.asignar_mision(astronauta, "Starship", "Marte", 275)
        director.registrar_evaluacion(astronauta, "Starship", "Exito", "Muy buena")

        director.generar_reporte_global([astronauta])
        ingeniero.supervisar_sistema("Paneles Solares", "Buenos")

        print(ingeniero.informe_personal())
        print(astronauta.informe_personal())

    except Exception as e:
        with open("reportes/log_errores.txt", "a") as log:
            log.write(f"[{datetime.now()}] Error: {str(e)}\n")
        print("Ocurrio un error. Revisa el archivo logerrores.txt.")


os.system("pause")