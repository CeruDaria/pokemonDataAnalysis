from urllib.parse import urljoin
import scrapy


class SpiderpkmattacksSpider(scrapy.Spider):
    name = 'spiderPkmAttacks'
    allowed_domains = ['www.serebii.net']
    start_urls = ['https://www.serebii.net/attackdex/']

    custom_settings = {
        'FEEDS': {'moves.csv': {'format': 'csv'}}
    }

    def parse(self, response):
        moves = response.xpath("//select[contains(@name,'SelectURL')]/option/b/option/@value").extract()
        
        for move in moves:
            url = urljoin(response.url, move)
            yield scrapy.Request(url, callback=self.parse_moves)

    def parse_moves(self, response):
        yield {
            "moveName": response.xpath("//table[@class='dextab']/tr[2]/td[1]/text()").extract_first().strip(),
            "type": response.xpath("//table[@class='dextab']/tr[2]/td[2]/div/img/@src").extract_first().partition("type/")[2].partition(".")[0],
            "pp": response.xpath("//table[@class='dextab']/tr[4]/td[@class='cen'][1]/text()").extract_first().strip(),
            "pwr": response.xpath("//table[@class='dextab']/tr[4]/td[@class='cen'][2]/text()").extract_first().strip(),
            "acc": response.xpath("//table[@class='dextab']/tr[4]/td[@class='cen'][3]/text()").extract_first().strip(),
            "desc": response.xpath("//table[@class='dextab']/tr[5]/td[@class='fooinfo']/text()").extract_first().strip(),
            "tm": response.xpath("//table[@class='dextab']/tr[8]/td[@class='cen'][1]/text()").extract_first().strip(),
        }