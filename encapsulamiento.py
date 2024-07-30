class Persona:
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f'Hola {self.nombre}'

    def getIdentificacion(self):
        return self.__identificacion

    def setIdentificacion(self, valor):
        self.__identificacion = valor


persona1 = Persona(45678, "Antonio", 45)
print(persona1.getIdentificacion())
persona1.setIdentificacion(12345)
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)
