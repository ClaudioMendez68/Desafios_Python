def promedio(lista):
    return sum(lista)/len(lista)

# Código alternativo SIN List Comprehension
"""
def alerta(lista):
    sobre_velocidad = []
    prom = promedio(lista)
    for i, velocidad in enumerate(lista):
        if velocidad > prom:
            sobre_velocidad.append(i)
    return sobre_velocidad
"""
# Código CON List Comprehension
def alerta(lista):
    prom = promedio(lista)
    return [i for i, velocidad in enumerate(lista) if velocidad > prom]

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

print(alerta(velocidad))