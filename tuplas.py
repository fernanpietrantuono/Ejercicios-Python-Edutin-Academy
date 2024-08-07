"""
Crear una tupla con números, luego pedir un número por teclado e indicar
cuántas veces se repite
"""
numeros = (5, 6, 7, 8, 5, 5, 6, 90, 12, 14, 12)
numero = int(input("Dame un número: "))
indices = []
if numero in numeros:
    if numeros.count(numero) == 1:
        print(f'El número {numero} se repite {numeros.count(numero)} vez en la tupla')
    else:
        print(f'El número {numero} se repite {numeros.count(numero)} veces en la tupla')
    for i, valor in enumerate(numeros):
        if valor == numero:
            indices.append(i)
    if len(indices) == 1:
        print(f'El número {numero} se encuentra en el índice {indices} de la tupla')
    else:
        print(f'El número {numero} se encuentra en los índices {indices} de la tupla')
else:
    print(f'Lo siento, el número {numero} no está en la tupla ☹')
