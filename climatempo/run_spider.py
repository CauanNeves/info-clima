import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from climatempo.spiders.clima import WeatherSpider

def run_weather_spider():
    runner = CrawlerRunner(
        settings={
            'FEEDS': {
                'weather_data.json': {'format': 'json'}, 
            },
        }
    )
    d = runner.crawl(WeatherSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

if __name__ == '__main__':
    run_weather_spider()
