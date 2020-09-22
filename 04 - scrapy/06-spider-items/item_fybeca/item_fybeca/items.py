 
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

## ../../images/thumbnail/294930.jpg
## https://www.fybeca.com/images/thumbnail/294930.jpg

def transformar_url_imagen(texto):
    url_fybeca = 'https://www.fybeca.com'
    cadena_texto = '../..'
    return texto.replace(cadena_texto, url_fybeca)

class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose( # Lista de funciones
            transformar_url_imagen
        ),
        output_proccesor = TakeFirst()  # Obtenemos una lista []
                                        # Sacamos el primero de la lista
    )







class ItemFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass