"""
def es_par(num):
    if num % 2 == 0:
        print(f'El número {num} es par')
    else:
        print(f'El número {num} es impar')


es_par(22)
"""

"""
def saludar(nombre):
    print(f'Hola {nombre}, sos el mejor programador')


saludar("Matías")
"""

"""
def resta(a=None, b=None):
    if a is None or b is None:
        print("¡Error! Tenés que enviar dos números a la función")
        return
    return a - b


print(resta(5, 2))
"""


def multplicacion(num=None):
    if num is None:
        print("Por favor, introducí un número")
    else:
        print(f'Tabla de multiplicar del {num}')
        for i in range(1, 11):
            print(f'{num} x {i} = {i * num}')


multplicacion(10)
