import scrapy


class SocymSpiderSpider(scrapy.Spider):
    name = 'socym_spider'
    allowed_domains = ['socym.co.jp']
    start_urls = ['http://socym.co.jp/book_genre/genre-programming']

    def parse(self, response):
        # get titles
        for title in response.css('.detail > h2'):
            yield {'title': title.css('h2::text').get()}

        # crawl to next page
        next_page = response.css('.nextpostslink::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
