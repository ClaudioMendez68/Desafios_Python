import getpass
from string import ascii_lowercase

set = ascii_lowercase
clave = getpass.getpass("Ingrese la contraseña: ")

intento = 0
for caracter in clave: #
    for letra in set:
        intento+= 1
        if caracter == letra:
           break
       
print(f"La contraseña fue forzada en {intento} intentos")