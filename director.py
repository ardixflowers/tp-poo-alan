from persona import *
from datetime import datetime

class DuracionNegativaError(Exception):
    pass

class Director(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)

    def asignar_mision(self, astronauta, nombre, destino, duracion):
        if duracion < 0:
            raise DuracionNegativaError("La duracion de una mision no puede ser negativa.")
        mision = {
            "nombre": nombre,
            "destino": destino,
            "duracion": duracion,
            "resultado": None,
            "evaluacion": None
        }
        astronauta.misiones.append(mision)
        with open("reportes/registro_misiones.txt", "a") as f:
            f.write(f"{astronauta.get_nombre()} asignado a mision {nombre} ({destino}, {duracion} dias)\n")

    def registrar_evaluacion(self, astronauta, nombre_mision, resultado, evaluacion):
        astronauta.registrar_resultado(nombre_mision, resultado, evaluacion)
        with open(f"reportes/evaluacion_{astronauta.get_nombre()}.txt", "a") as f: 
            f.write(f"Mision: {nombre_mision}, Resultado: {resultado}, Evaluacion: {evaluacion}\n")

    def generar_reporte_global(self, lista_astronautas):
        reporte = f"reportes/Reporte Global - {datetime.now()}\n\n"
        for astro in lista_astronautas:
            reporte += astro.informe_personal() + "\n"
        with open("reportes/reporte_global.txt", "w") as f:
            f.write(reporte)