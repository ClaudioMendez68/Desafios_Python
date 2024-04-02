
def validate(opciones, eleccion):
    """ Valida los valores ingresados,
        repitiendo la petición hasta que los valores sean los correctos
    Args:
        opciones (list): Lista de valores a comparar
        eleccion (Any): Opción a validar

    Returns:
        Any: Opción validada
    """
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ').lower()
    
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    