"""
Primer ejemplo:
Crear un programa que reciba el n° de años que tiene la computadora.
Imprimir en consola si es nueva o es vieja
Condiciones: menor o igual a 2 años se califica como nueva, caso contrario
se considera como vieja
"""

antiguedad = int(input("Ingresá la antigüedad de tu computadora: "))
if 0 <= antiguedad <= 2:
    print("Tu computadora es nueva")
else:
    print("Tu computadora es vieja")

edad = int(input("¿Cuántos años tenés? "))
if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
print("¡Adiós!")
