class Vehiculo:
    def __init__(self, marca, modelo, color, patente):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.patente = patente
        self.avanza = False
        self.frena = False
        self.gira = False

    def avanzar(self):
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f'Marca: {self.marca} \n'
              f'Modelo: {self.modelo} \n'
              f'Color: {self.color} \n'
              f'Patente: {self.patente} \n'
              f'Avanzar: {self.avanza} \n'
              f'Frenar: {self.frena} \n'
              f'Girar: {self.gira} \n')


class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, patente, cilindrada):
        super().__init__(marca, modelo, color, patente)
        self.cilindrada = cilindrada


moto1 = Moto("Aprilia", "Tuareg 660", "Azul", "A123BCD", 660)
moto1.avanzar()
moto1.frenar()
moto1.girar()
print(f'Cilindrada: {moto1.cilindrada}')
moto1.imprimir()
