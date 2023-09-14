import scrapy


class TmtcSpider(scrapy.Spider):
    name = "tmtc"
    allowed_domains = ["tmt.my"]
    start_urls = ["https://www.tmt.my/products/products-search?search=g502"]

    def parse(self, response):
        pass
