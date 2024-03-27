import sys

# Se utliza estructura de lista proporcionada por argv
sol_peruano = float(sys.argv[1])
peso_argentino= float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = float(sys.argv[4])

# Se realizan las operaciones de conversión y visualización de resultados
print(f'Los {peso_chileno} pesos equivalen a:')
print(f'{sol_peruano * peso_chileno} Soles')
print(f'{peso_argentino * peso_chileno} Pesos Argentinos')
print(f'{dolar_americano * peso_chileno} Dólares')