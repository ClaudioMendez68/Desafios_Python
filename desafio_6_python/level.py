def choose_level(n_pregunta, p_level):
    """Escoge el nivel de dificultad de la pregunta

    Args:
        n_pregunta (int): Número de la pregunta
        p_level (int): Nivel escogido

    Returns:
        str : Nivel escogido
    """
    # Construir lógica para escoger el nivel
    ##################################################

    if  n_pregunta <= p_level:
            level = 'basicas'
    elif n_pregunta <= 2*p_level:
            level = 'intermedias'
    elif n_pregunta <= 3*p_level:
            level = 'avanzadas'
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias