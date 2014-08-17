import scrapy

class WebSpider(scrapy.Spider):
    name = "Web"
    allowed_domains = ["https://developers.google.com/groups/pulse/India"]
    start_urls = [
        "https://developers.google.com/groups/pulse/India"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)