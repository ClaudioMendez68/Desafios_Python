from get_birds import get_request

lista_aves = get_request('https://aves.ninjas.cl/api/birds')
def get_images(resolucion):
    """Extrae los enlaces a las imágenes de las aves desde la API y los almacena en una lista

    Args:
        resolucion (str): ['main']['full']['thumb'] Resolución a la que se desea la imagen

    Returns:
        list: Lista de todos los enlaces a las imágenes de las aves según la resolución elegida
    """
    return [imagen['images'][resolucion] for imagen in lista_aves]

if __name__ == '__main__':
    print(get_images('full'))