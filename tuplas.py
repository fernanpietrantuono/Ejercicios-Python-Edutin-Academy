"""
Crear una tupla con números, luego pedir un número por teclado e indicar
cuántas veces se repite
"""
numeros = (5, 6, 7, 8, 5, 5, 6, 90, 12, 14, 12)
numero = int(input("Dame un número: "))
if numeros.count(numero) == 1:
    print(f'El número {numero} se repite {numeros.count(numero)} vez')
else:
    print(f'El número {numero} se repite {numeros.count(numero)} veces')
print(f'El número {numero} se encuentra en el índice {numeros.index(numero)}')
