import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod div.product_price p.price_color'
        )
        # etiqueta_conte = response.css("article.product_pod div.image_container") 
        # etiqueta_conte = response.css("article.product_pod div.product_price p.instock") 
        titulos = etiqueta_contenedora.css(
            '::text'
        ).extract()
        #imagen = etiqueta_conte.css('a > img::attr(src)').extract()
        #stock = etiqueta_conte.css('::text').extract()
        print(titulos)
        print(type(titulos))
        print(len(titulos))

# scrapy crawl nombre_arania