import scrapy


class SpiderpkmlearnedmovesSpider(scrapy.Spider):
    name = 'spiderPkmLearnedMoves'
    allowed_domains = ['www.serebii.net']
    start_urls = []
    for i in range(1, 152):
        i = str(i).zfill(3)
        url = f'https://www.serebii.net/pokedex-rs/{i}.shtml'
        start_urls.append(url)

    custom_settings = {
        'FEEDS': {'pokemons_learned_moves.csv': {'format': 'csv'}}
    }

    def parse(self, response):
        pkm = response.xpath("//td[@class='tooltabcon'][1]/text()").extract_first().strip()
        pkdNo = response.xpath("//table[@class='dextable'][1]/tr[2]/td[@class='fooinfo'][2]/text()").extract_first().strip()

        # Level up
        table_length = len(response.xpath("//table[@class='dextable' and contains(.,'Fire Red/Leaf Green Level Up')]/tbody/tr").extract())
        
        for i in range(1, table_length, 2):
            results = {
                "pkdNo": pkdNo,
                "pkmName": pkm,
                "attackName": response.xpath(f"//table[@class='dextable' and contains(.,'Fire Red/Leaf Green Level Up')]/tbody/tr[{i}]/td[@class='fooinfo'][2]/a/text()").extract(),
                "cond": "Level Up",
                "req": response.xpath(f"//table[@class='dextable' and contains(.,'Fire Red/Leaf Green Level Up')]/tbody/tr[{i}]/td[@class='fooinfo'][1]/text()").extract()
            }
            yield results

        # TM & HM Attacks
        table_length = len(response.xpath("//table[@class='dextable' and contains(.,'TM & HM Attacks')]/tbody/tr").extract())
        
        for i in range(1, table_length, 2):
            results = {
                "pkdNo": pkdNo,
                "pkmName": pkm,
                "attackName": response.xpath(f"//table[@class='dextable' and contains(.,'TM & HM Attacks')]/tbody/tr[{i}]/td[@class='fooinfo'][2]/a/text()").extract(),
                "cond": "TM & HM",
                "req": response.xpath(f"//table[@class='dextable' and contains(.,'TM & HM Attacks')]/tbody/tr[{i}]/td[@class='fooinfo'][1]/text()").extract()
            }

            yield results

        # Fire Red/Leaf Green/Emerald Tutor Attacks
        table_length = len(response.xpath("//table[@class='dextable' and contains(.,'Fire Red/Leaf Green/Emerald Tutor Attacks')]/tbody/tr").extract())
        
        for i in range(1, table_length, 2):
            results = {
                "pkdNo": pkdNo,
                "pkmName": pkm,
                "attackName": response.xpath(f"//table[@class='dextable' and contains(.,'Fire Red/Leaf Green/Emerald Tutor Attacks')]/tbody/tr[{i}]/td[@class='fooinfo']/a/text()").extract(),
                "cond": "Tutor",
                "req": ""
            }

            yield results

        # Egg Moves
        table_length = len(response.xpath("//table[@class='dextable' and contains(.,'Egg Moves')]/tbody/tr").extract())
        
        for i in range(1, table_length, 2):
            results = {
                "pkdNo": pkdNo,
                "pkmName": pkm,
                "attackName": response.xpath(f"//table[@class='dextable' and contains(.,'Egg Moves')]/tbody/tr[{i}]/td[@class='fooinfo']/a/text()").extract(),
                "cond": "Egg",
                "req": ""
            }

            yield results

        

