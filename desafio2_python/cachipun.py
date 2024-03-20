# Se importa el método choice de la librería random
from random import choice

print("********************************************************************")
print("              JUEGA AL CACHIPÚN CONTRA EL COMPUTADOR")
print("********************************************************************")

# Se define el set de jugadas posibles a realizar por el computador
cachipun= ["piedra", "papel", "tijera"]
computador= choice(cachipun)

# Se ingresa jugada por parte del usuario y se convierte palabra ingresada a minúsculas para validaciones posteriores
usuario= input("Ingresa tu jugada [piedra, papel o tijera]: ")
usuario= usuario.lower()

# Validación de término correcto en la entrada. Si el término es incorrecto, se vuelve a solicitar jugada.
while usuario != "piedra" and usuario != "papel" and usuario != "tijera":
    print("Jugada NO VÁLIDA")
    usuario= input("Ingresa tu jugada [piedra, papel o tijera]: ")
    usuario= usuario.lower()

# Se ejecuta la jugada si pasa la validación
print(f"Jugaste: {usuario}")
print(f"El computador jugó: {computador}") 

# Evaluación de posibles combinatorias del juego
if usuario == "piedra" and computador == "tijera":
    print("¡GANASTE!")
elif usuario == "papel" and computador == "piedra":
    print("¡GANASTE!")
elif usuario == "tijera" and computador == "papel":
    print("¡GANASTE!")
elif usuario == computador:
    print("¡EMPATASTE!")
else:
    print("¡PERDISTE!")