"""
En una autoescuela hay un programa que, depende de la edad de la persona,
debe mostrar el tipo de licencia.
Condiciones:
1. Si es menor a 16, no debe manejar
2. Si es menor a 18, puede obtener un permiso de conducción
3. Si es menor a 70, obtiene un carnet estándar
4. Si es mayor a 70, necesita una licencia especial
"""
edad = int(input("¿Cuántos años tenés? "))
if edad < 16:
    print("No estás apto para manejar")
elif 16 <= edad < 18:
    print("Podés obtener un permiso de conducción")
elif 18 <= edad < 70:
    print("Podés conseguir un carnet estándar")
else:
    print("Necesitás un carnet especial")
