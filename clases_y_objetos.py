class Bicicleta:
    def __init__(self, color, cambios, rodado):
        self.color = color
        self.cambios = cambios
        self.rodado = rodado

    @staticmethod
    def frenar():
        return "La bici está frenando."

    @staticmethod
    def avanzar():
        return "La bici está en movimiento"

    @staticmethod
    def girar():
        return "La bici está girando"


urbana = Bicicleta("Rojo", 6, 26)
hibrida = Bicicleta("Blanco", 8, 29)
print(f'Urbana: {urbana.color}')
print(f'Comportamiento de la bici urbana: {urbana.girar()}')
print("\n")
print(f'Híbrida: {hibrida.cambios}')
print(f'Comportamiento de la bici híbrida: {hibrida.avanzar()}')
