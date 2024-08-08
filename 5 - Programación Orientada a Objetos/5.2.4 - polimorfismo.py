class Gato:
    @staticmethod
    def sonido():
        print("Miau")


class Perro:
    @staticmethod
    def sonido():
        print("Guau")


class Cerdo:
    @staticmethod
    def sonido():
        print("Oing Oing")


def escucharSonido(animal):
    animal.sonido()


gato1 = Gato()
perro1 = Perro()
cerdo1 = Cerdo()

escucharSonido(gato1)
escucharSonido(perro1)
escucharSonido(cerdo1)
