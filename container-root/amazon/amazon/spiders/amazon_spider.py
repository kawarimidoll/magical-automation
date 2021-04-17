import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    def parse(self, response):
        pass
