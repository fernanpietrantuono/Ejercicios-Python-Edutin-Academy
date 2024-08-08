# Calculadora del índice de masa corporal
cont = 0
print("Calculadora del índice de masa corporal (IMC)\n")
while cont != 2:
    cont = int(input("¿Querés seguir calculando el IMC? 1: Sí y 2:No \n"))
    if cont == 1:
        altura = float(input("Ingresá tu altura en metros: "))
        peso = float(input("Ingresá tu peso en kg: "))
        imc = round(peso / (altura ** 2), 2)
        if imc < 18.5:
            print(f'IMC {imc} = Peso bajo')
        elif 18.5 < imc < 24.99:
            print(f'IMC {imc} = Peso normal')
        elif 25 < imc < 30:
            print(f'IMC {imc} = Sobrepeso')
        elif imc > 30:
            print(f'IMC {imc} = Obesidad')
    elif cont == 2:
        print("Adiós!")
print("Gracias por usar la calculadora de IMC")
