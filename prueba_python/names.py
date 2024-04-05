from get_birds import get_request

lista_aves = get_request('https://aves.ninjas.cl/api/birds')
def get_names(lenguaje):
    """Extrae los nombres de las aves desde la API y los almcena en una lista

    Args:
        lenguaje (str): ['spanish']['english'] Lenguaje en que estarán los nombres

    Returns:
        list: Lista de todos los nombres de las aves en el lenguaje seleccionado.
    """
    return [ave['name'][lenguaje] for ave in lista_aves]

if __name__ == '__main__':
    print(get_names('english'))
    print(get_names('spanish'))