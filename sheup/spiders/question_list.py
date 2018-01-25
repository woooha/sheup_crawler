import scrapy

class SheupSpider(scrapy.spiders.Spider):
    name = 'sheup'
    allowed_domains = ["www.sheup.net"]
    start_urls = [
        "http://www.sheup.net/info_tiku_4.php?type=1",
        "http://www.sheup.net/info_tiku_4.php?type=2",
        "http://www.sheup.net/info_tiku_4.php?type=3",
        "http://www.sheup.net/info_tiku_4.php?type=4",
        "http://www.sheup.net/info_tiku_4.php?type=5",
        "http://www.sheup.net/info_tiku_4.php?type=6",
        "http://www.sheup.net/info_tiku_4.php?type=7",
        "http://www.sheup.net/info_tiku_4.php?type=8",
        "http://www.sheup.net/info_tiku_4.php?type=10",
        "http://www.sheup.net/info_tiku_4.php?type=11",
        "http://www.sheup.net/info_tiku_4.php?type=12",
        "http://www.sheup.net/info_tiku_4.php?type=13",
        "http://www.sheup.net/info_tiku_4.php?type=14",
        "http://www.sheup.net/info_tiku_4.php?type=15",
        "http://www.sheup.net/info_tiku_4.php?type=17",
        "http://www.sheup.net/info_tiku_4.php?type=18",
        "http://www.sheup.net/info_tiku_4.php?type=20",
        "http://www.sheup.net/info_tiku_4.php?type=21",
    ]

    def parse(self, response):
        anchors = response.css('.tiku_2 a').xpath('@href').extract()
        for anchor in anchors:
            print response.urljoin(anchor)
        for href in response.css('.pagecss a::attr(href)'):
            yield response.follow(href, self.parse)
