import scrapy
import re


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.co.jp']
    start_urls = [
        'http://amazon.co.jp/dp/4802611080',
        'http://amazon.co.jp/dp/480261179X'
    ]

    def parse(self, response):
        feature_div = response.xpath(
            '//div[@id="detailBulletsWrapper_feature_div"]')
        spans = feature_div.xpath(
            '//span[@class="a-list-item"]/text()').getall()
        ranking = [s for s in spans if re.match('.*位.*', s)]

        # 書籍では以下の形式だが現在はこのIDはページ内に存在しない
        # Amazonの仕様がかわったのかもしれないがどちらにしろ取得は無理
        # ranking = response.css('#SalesRank')

        yield {'ranking': ranking}
