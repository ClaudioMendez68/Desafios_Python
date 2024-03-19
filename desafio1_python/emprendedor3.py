print("******************************************************")
print("   CÁLCULO DE RENTABILIDAD E INDICE DE CRECIMIENTO")
print("******************************************************")

# Ingreso y almacenamiento de variables en formato numérico
precio = float(input("Ingrese el precio de la suscripción $: "))
usuario = int(input("Ingrese el número de usuarios: "))
gasto_total = float(input("Ingrese el gasto total $: "))
utilidad_anterior = float(input("Ingrese las utiolidades del año anterior $: "))

# Cálculo de la utilidad e índice de crecimiento
utilidad = precio*usuario - gasto_total
indice = utilidad/utilidad_anterior

# Visualización de la utilidad y el índice de crecimiento por consola
print(f"La utilidad del período es de ${round(utilidad)}.-")
print(f"El índice de crecimiento de la utilidad respecto del año pasado es de: {round(indice, 2)}")