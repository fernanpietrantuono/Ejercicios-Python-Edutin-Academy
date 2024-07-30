"""
add // Añade un elemento al final del conjunto
clear // Elimina toda la información del conjunto
pop // Devuelve y elimina un elemento arbitrario o devuelve un error si está vacío
remove // Intenta eliminar un elemento del conjunto, si no existe, elevará un error
union // Devuelve un conjunto con todos los elementos de ambos conjuntos
"""

# 1° forma
alumnos = {"Andrea", "Ruby", "Marcos", "Marlon", "José"}
# print(alumnos)

# 2° forma
lenguajes = set(["PHP", "Java", "Python", "C", "C++"])
# print(lenguajes)
# lenguajes.add("C#")
# lenguajes.clear()
# lenguajes.pop()
# lenguajes.remove("C++")
todos = alumnos.union(lenguajes)
print(todos)
