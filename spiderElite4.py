import scrapy


class Spiderelite4Spider(scrapy.Spider):
    name = 'spiderElite4'
    allowed_domains = ['https://www.serebii.net']
    start_urls = ['http://www.serebii.net/fireredleafgreen/elitefour.shtml']

    custom_settings = {
        'FEEDS': {'elite4.csv': {'format': 'csv'}}
    }

    def parse(self, response):
        for i in range(2,9,2):
            yield {
                "name": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[1]/text()").extract_first().strip(),
                "pkm1": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[2]/text()").extract_first().strip(),
                "pkm2": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[3]/text()").extract_first().strip(),
                "pkm3": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[4]/text()").extract_first().strip(),
                "pkm4": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[5]/text()").extract_first().strip(),
                "pkm5": response.xpath(f"//table[@class='tab'][1]/tr[{i}]/td[@class='foocontent']/table[@class='trainer']/tr[2]/td[6]/text()").extract_first().strip(),
                "pkm6": "na"
            }

        for j in range(1,4):
            yield {
                "name": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[1]/text()").extract_first(),
                "pkm1": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[2]/text()").extract_first(),
                "pkm2": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[3]/text()").extract_first(),
                "pkm3": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[4]/text()").extract_first(),
                "pkm4": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[5]/text()").extract_first(),
                "pkm5": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[6]/text()").extract_first(),
                "pkm6": response.xpath(f"//table[@class='tab'][1]/tr[10]/td[@class='foocontent']/table[@class='trainer'][{j}]/tr[2]/td[7]/text()").extract_first(),
            }