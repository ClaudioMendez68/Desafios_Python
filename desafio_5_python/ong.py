
def factorial(numero):
    fact = 1
    for i in range(1, numero+1):
        fact = fact * i
    return fact

def productoria(lista):
    prod = 1
    for num in lista:
        prod = prod*num
    return prod
# En la función "calcular()"" se incorporan algunos validadores para sus parámetros
def calcular(**argumentos):
    for arg in argumentos:
        if 'fact_' in arg:
            # En esta validación se considera el borde "0! = 1"
            if type(argumentos[arg]) == int and argumentos[arg] >= 0:
                print(f'El factorial de {argumentos[arg]} es {factorial(argumentos[arg])}')
            else:
                print(f'El argumento "{arg}" DEBE ser un número entero no negativo')
        elif 'prod_' in arg:
            if type(argumentos[arg]) == list and len(argumentos[arg]) > 0:
                print(f'La productoria de {argumentos[arg]} es {productoria(argumentos[arg])}')
            else:
                print(f'El argumento "{arg}" DEBE escribirse entre corchetes "[]" y no estar vacío')

calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)