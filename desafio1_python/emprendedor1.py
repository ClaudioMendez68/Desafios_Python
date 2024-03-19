print("*****************************************")
print("        CÁLCULO DE RENTABILIDAD")
print("*****************************************")

# Ingreso y almacenamiento de variables en formato numérico
precio = float(input("Ingrese el precio de la suscripción $: "))
usuario = int(input("Ingrese el número de usuarios: "))
gasto_total = float(input("Ingrese el gasto total $: "))

# Cálculo de la utilidad
utilidad = precio*usuario - gasto_total

# Visualización de la utilidad por consola
print(f"La utilidad del período es de ${round(utilidad)}.-")