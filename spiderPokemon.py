import enum
import scrapy


class SpiderpokemonSpider(scrapy.Spider):
    name = 'spiderPokemon'
    allowed_domains = ['www.serebii.net']
    start_urls = []
    for i in range(1, 20):
        i = str(i).zfill(3)
        url = f'https://www.serebii.net/pokedex-rs/{i}.shtml'
        start_urls.append(url)

    custom_settings = {
        'FEEDS': {'pokemons.csv': {'format': 'csv'}}
    }

    def parse(self, response):
        type_order = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fight', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel']
        base_stats = response.xpath("//table[@class='dextable']/tr[contains(.,'Base Stats')]//text()").extract()

        results = {
        'pkdNo': response.xpath("//table[@class='dextable'][1]/tr[2]/td[@class='fooinfo'][2]/text()").extract_first().strip(),
        'pkmName': response.xpath("//td[@class='tooltabcon'][1]/text()").extract_first().strip(),
        'type1': response.xpath("//table[@class='dextable'][1]/tr[8]/td[@class='fooinfo'][2]/div/a/img/@src").extract_first().partition("type/")[2].partition(".")[0],
        'type2': response.xpath("//table[@class='dextable'][1]/tr[8]/td[@class='fooinfo'][3]/div/a/img/@src").extract_first().partition("type/")[2].partition(".")[0],
        'hp': base_stats[1],
        'atk': base_stats[2],
        'def': base_stats[3],
        'spAtk': base_stats[4],
        'spDef': base_stats[5],
        'spd': base_stats[6],
        }

        abilities = response.xpath("//table[@class='dextable'][1]/tr[3]/td[@class='fooinfo'][2]/b/text()").extract_first().partition("Ability: ")[2]
        abl_desc = response.xpath("//table[@class='dextable'][1]/tr[4]/td[@class='fooinfo']/text()").extract()
        results["ability1"] = abilities.partition(" & ")[0] if "&" in abilities else abilities
        results["ability2"] = abilities.partition(" & ")[2] if "&" in abilities else "na"
        if len(abl_desc) == 1:
             results["abl1Desc"] = abl_desc[0].strip()
             results["abl2Desc"] = "na"
        else:
            results["abl1Desc"] = abl_desc[1].replace(": ","").strip()
            results["abl2Desc"] = abl_desc[2].replace(": ","").strip()

        for i, type in enumerate(type_order):
            results[f'{type}DamageTaken'] = response.xpath(f"//table[@class='dextable'][3]/tr[3]/td[@class='footype'][{i+1}]/text()").extract_first().partition("*")[2]

        yield results
