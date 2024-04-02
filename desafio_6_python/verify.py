import preguntas as p


def verificar(alternativas, eleccion):
    """Verifica si la respuesta entregada por el usuario es correcta e informa el resultado

    Args:
        alternativas (list): Lista de listas con alternativas
        eleccion (str): Elección realizada por el usuario

    Returns:
        bool: Resultado de la verificación
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if alternativas[eleccion][1] == 1:
        print("Respuesta Correcta")
        correcto = True
    else:
        print("Respuesta Incorrecta")
        correcto = False 
        
    ##########################################################################################
    return correcto


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)





