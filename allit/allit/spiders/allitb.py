import scrapy


class AllitbSpider(scrapy.Spider):
    name = "allitb"
    allowed_domains = ["allithypermarket.com.my/"]
    start_urls = ["https://www.allithypermarket.com.my/search?type=product&options%5Bunavailable_products%5D=last&options%5Bprefix%5D=last&q=g502"]

    def parse(self, response):
        pass