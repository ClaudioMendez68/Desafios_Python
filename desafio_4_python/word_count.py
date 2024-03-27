from sys import argv

# Se captura el archivo de texto a procesar nmediante argv y se asigna a la variable texto
with open(argv[1], "r") as file:
    texto= file.read()
# Se separan los caracteres contenidos en la variable texto y se asignan a la variable palabras como una lista
# mediante el método split()
palabras = texto.split()
# Se convierte el contenido string del archivo 'texto' en un set para generar un conjunto de caracteres no duplicados
caracteres = set(texto)
# Se convierte la lista 'palabras' en un set para generar un conjunto de palabras no duplicadas y se asigna a 
# la variable 'palabras_distintas'
palabras_distintas = set(palabras)

# Como los sets 'caracteres' y 'palabras_distintas' contienen elementos no duplicados, se obtiene la cantidad mediante
# el tamaño de cada conjunto
print(f'El número de caracteres distintos es: {len(caracteres)}')
print(f'El número de palabras distintas es: {len(palabras_distintas)}')