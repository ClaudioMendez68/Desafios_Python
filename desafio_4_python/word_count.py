from sys import argv

with open(argv[1], "r") as file:
    texto= file.read()

palabras = texto.split()
caracteres = set(texto)
palabras_distintas = set(palabras)

print(f'El número de caracteres distintos es: {len(caracteres)}')
print(f'El número de palabras distintas es: {len(palabras_distintas)}')