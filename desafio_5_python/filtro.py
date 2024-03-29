from sys import argv

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

umbral = int(argv[1])

# Código alternativo SIN List Comprehension
"""
filtro = []
def mayores(precios, umbral):
    for  producto in precios:
        if precios[producto] > umbral:
            filtro.append(producto)
    return filtro

def menores(precios, umbral):
    for producto in precios:
        if precios[producto] < umbral:
            filtro.append(producto)
    return filtro 
"""
# Código CON List Comprehension
def mayores(precios, umbral):
    return [producto for producto in precios if precios[producto] > umbral]

def menores(precios, umbral):
    return [producto for producto in precios if precios[producto] < umbral]

if len(argv) == 2:
    print(f'Los productos mayores al umbral son: {', '.join(mayores(precios, umbral))}')
elif argv[2] == 'menor':
    print(f'Los productos menores al umbral son: {', '.join(menores(precios, umbral))}')
else:
    print('Lo sentimos, no es una operación válida')