from persona import *

class Astronauta(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.misiones = []  #diccionarios con info de misiones

    def registrar_resultado(self, nombre_mision, resultado, evaluacion):
        for mision in self.misiones:
            if mision['nombre'] == nombre_mision:
                mision['resultado'] = resultado
                mision['evaluacion'] = evaluacion
                break

    def informe_personal(self):
        info = super().informe_personal()
        info += "Misiones:\n"
        for i in self.misiones:
            info += f"  - {i['nombre']} a {i['destino']} ({i['duracion']} dias) Resultado: {i['resultado']}, Evaluacin: {i['evaluacion']}\n"
        return info