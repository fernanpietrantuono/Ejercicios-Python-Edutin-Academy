"""
edad = int(input("¿Cuántos años tenés? "))
egreso = input("¿Ya egresaste? Respondé si o no: ")
if edad > 18:
    print("Felicitaciones!!! Ahora sos mayor de edad")
    if egreso == "si":
        print("Felicitaciones por tu egreso!!!")
"""
password = input("Creá una contraseña: ")
if len(password) >= 8:
    print("La contraseña que creaste es aceptable")
    if password == "Prueba12345":
        print("Además, es la contraseña correcta")
    else:
        print("Pero es incorrecta")
else:
    print("La contraseña que creaste es incorrecta e insegura.")
