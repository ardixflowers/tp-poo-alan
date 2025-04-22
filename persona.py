class DatosIncompletosError(Exception):
    pass

class Persona:
    def __init__(self, nombre, dni, nacionalidad):
        if not nombre or not dni or not nacionalidad:
            raise DatosIncompletosError("Todos los datos de la persona son obligatorios.")
        self.__nombre = nombre
        self.__dni = dni
        self.__nacionalidad = nacionalidad

    def get_nombre(self):
        return self.__nombre

    def informe_personal(self):
        return f"Nombre: {self.__nombre}\nDNI: {self.__dni}\nNacionalidad: {self.__nacionalidad}\n"