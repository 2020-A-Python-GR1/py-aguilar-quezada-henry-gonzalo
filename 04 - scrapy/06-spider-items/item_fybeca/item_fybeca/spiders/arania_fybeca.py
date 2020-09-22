# arania_fybeca.py
import scrapy
from item_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaFybeca(scrapy.Spider):
    name = 'fybeca'
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
    ]
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)
            
    def parse(self, response):
        productos = response.css('div.product-tile-inner')