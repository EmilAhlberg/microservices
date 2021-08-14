from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from steamscraper.spiders.steam_spider import SteamSpider


process = CrawlerProcess(get_project_settings())
process.crawl(SteamSpider)
process.start()
