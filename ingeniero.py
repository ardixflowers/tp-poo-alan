from persona import *

class SistemaRepetidoError(Exception):
    pass

class Ingeniero(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.sistemas = []

    def supervisar_sistema(self, sistema, estado):
        if any(s[0] == sistema for s in self.sistemas):
            raise SistemaRepetidoError(f"El sistema '{sistema}' ya ha sido supervisado.")
        self.sistemas.append((sistema, estado))

    def informe_personal(self):
        info = super().informe_personal()
        info += "Sistemas supervisados:\n"
        for sistema, estado in self.sistemas:
            info += f"  - {sistema}: {estado}\n"
        return info