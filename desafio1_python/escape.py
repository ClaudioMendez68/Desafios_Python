from math import  sqrt

print("*****************************************")
print("        VELOCIDAD MÍNIMA DE ESCAPE")
print("*****************************************")

# Ingreso y almacenamiento de variables en formato numérico
gravedad = float(input("Ingrese la constante gravitacional del planeta en [m/s^2]: "))
radio = float(input("Ingrese el radio del planeta en [Kms]: "))

# Cálculo de la velocidad mínima de escape del planeta incluyendo la transformación de kilómetros a metros
velocidad_escape = sqrt(2*gravedad*radio*1000)

# Visualización del resultado por consola
print (f"La velocidad de escape del planeta es: {round(velocidad_escape, 1)} [m/s]")