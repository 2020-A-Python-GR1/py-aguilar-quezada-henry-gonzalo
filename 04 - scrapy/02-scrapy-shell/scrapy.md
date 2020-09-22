# Srapy
## Scrapy instalacion

Ejecutar dentro del `Anaconda prompt`.

```
$ pip install scrapy
```

## Comandos generales

Da `las caracteristicas` para poder hacer Web Scraping o Web Crawling de ese computador

```
$ scrapy bench
```
Visualizar las `configuraciones extra`

```
$ scrapy settings
```

Visualizamos la `version` de Scrapy
```
$ scrapy version
```

### scrapy view `url`

`Visualizar el contenido` como lo ve el Scrapy

Si se ve el contenido

```
$ scrapy view https://www.pluralsight.com/authors
```

No se ve el contenido
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scrapy shell `url`

Permite `interactuar con la respuesta` del scrapy mediante un `shell`
```
$ scrapy shell http://quotes.toscrape.com/
$ response.css('title')
$ response.css('title').extract()
$ response.css('title::text').extract()
$ response.css('.author').extract()
$ response.css('.author::text').extract()
$ type(response.css('.author::text'))
$ type(response.css('.author::text')[0])
$ response.css('.author').extract_first()
$ response.css('a::attr(href)').extract_first()
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()

$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()

```

## scrapy startproject `nombre_proyecto`

```
$ scrapy startproject arania_basica
```