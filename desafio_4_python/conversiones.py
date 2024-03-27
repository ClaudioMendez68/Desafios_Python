import sys

# Se crea estructura de diccionario
conversion = {
    'sol_peruano' : float(sys.argv[1]),
    'peso_argentino': float(sys.argv[2]),
    'dolar_americano' : float(sys.argv[3]),
    'peso_chileno' : int(sys.argv[4])
}
# Se realizan las operaciones de conversión y visualización de resultados
print(f'Los {conversion['peso_chileno']} pesos equivalen a:')
print(f'{conversion['sol_peruano'] * conversion['peso_chileno']} Soles')
print(f'{conversion['peso_argentino'] * conversion['peso_chileno']} Pesos Argentinos')
print(f'{conversion['dolar_americano'] * conversion['peso_chileno']} Dólares')