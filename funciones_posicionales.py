"""
def sumatoria(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma


print(sumatoria(3, 4, 5))
print(sumatoria(3, 4, 5, 7, 8, 9, 15, 16, 23, 78))
print(sumatoria(3, 4, 5, 6, 78))
print(sumatoria(10, 10, 10))
"""


"""
def lenguaje(nombre, *lenguajes):
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {lenguajes}')


lenguaje("Fernán", "Java", "JavaScript", "Python", "PHP", "C", "C++")
"""


def lenguaje(nombre, **kwargs):
    print(f'Hola {nombre}')
    print("Buscando información sobre tus lenguajes favoritos...")
    print("Cargando información... \n")
    print("Información: ")
    cont = 0
    print(type(kwargs))
    for clave in kwargs:
        cont += 1
        print(f'Tu {cont}° lenguaje favorito es: {kwargs[clave]}')


lenguaje("Tuchito", lenguaje1="Java", lenguaje2="JavaScript", lenguaje3="Python",
         lenguaje4="PHP", lenguaje5="C", lenguaje6="C++")
