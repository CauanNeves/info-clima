from typing import Any
import scrapy
from scrapy.http import Response

#CamleCase
class WeatherSpider(scrapy.Spider):
    #Nome do bot
    name = 'weatherbot'

    #Request
    def start_requests(self):
        urls = ['https://www.tempo.com/angra-dos-reis.htm']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    #Response
    def parse(self, response):
        for element in response.xpath('//ul[@class="grid-container-7 dias_w"]/li'):
            yield {
                'date': element.xpath('.//span[@class="text-0"]/text()').get(),
                'condition': element.xpath('.//img/@alt').get(),
                'max': element.xpath('.//span[@class="temp"]/span[1]/text()').get(),
                'min': element.xpath('.//span[@class="temp"]/span[3]/text()').get()
            }
