print("*********************************************************")
print("        CALCULE SU ÍNDICE DE MASA CORPORAL (IMC)")
print("*********************************************************")

# Ingreso y validación del peso
peso= int(input("Ingrese su peso en kilogramos:\n "))
while peso <= 0:
    print("Valor de peso INCORRECTO")
    peso= int(input("Ingrese su peso en kilogramos:\n"))

# Validación de la estatura    
estatura= int(input("Ingrese su estatura en centímetros:\n"))
while estatura <= 0:
    print("Valor de estatura INCORRECTO")
    estatura= int(input("Ingrese su estatura en centímetros:\n"))

# Cálculo del Índice de Masa Corporal
imc= peso/((estatura/100)**2)

print(f"Su Índice de Masa Corporal (IMC) es:\n {round(imc, 2)}")

# Clasificación OMS
if imc < 18.5:
    print("Usted clasifica como Bajo Peso")
elif imc >=18.5 and imc < 25:
    print("Usted clasifica como Adecuado")
elif imc >=25 and imc < 30:
    print("Usted clasifica como Sobrepeso")
elif imc >=30 and imc < 35:
    print("Usted clasifica como Obesidad I")
elif imc >=35 and imc < 40:
    print("Usted clasifica como Obesidad II")
else:
    print("Usted clasifica como Obesidad III")