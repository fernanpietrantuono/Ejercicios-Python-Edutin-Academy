"""
word = input("Ingresá una palabra: ")
for iterar in range(10):
    print(word)
"""

"""
print("Inicio")
cont = 1
for i in [3, 4, 5, 7, 8]:
    print(f'{cont}° vuelta')
    print(f'Hola, ahora i vale {i} y su cuadrado es {i ** 2}')
    cont += 1
print("Fin")
"""

num = int(input("Ingresá cualquier número para ver la tabla de multiplicar: "))
print(f'\nTabla de multiplicar del {num}')
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
