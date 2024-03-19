print("*****************************************")
print("        CÁLCULO DE RENTABILIDAD")
print("*****************************************")

# Ingreso y almacenamiento de variables en formato numérico
precio = float(input("Ingrese el precio de la suscripción $: "))
usuario_normal = int(input("Ingrese el número de usuarios normales: "))
usuario_premium = int(input("Ingrese el número de usuarios premium: "))
gasto_total = float(input("Ingrese el gasto total $: "))

# Cálculo de la utilidad, incluyendo la proporción del precio para usuarios premium
utilidad = precio*usuario_normal + 1.5*precio*usuario_premium - gasto_total

# Visualización de la utilidad por consola
print(f"La utilidad del período es de ${round(utilidad)}.-")