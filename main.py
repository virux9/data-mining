import os
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import dotenv

# from gb_parse.spiders.autoyoula import AutoyoulaSpider
# from gb_parse.spiders.hh import HeadHunterSpider
from gb_parse.spiders.instagram import InstagramSpider

# from gb_parse import settings

dotenv.load_dotenv('.env')

if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule('gb_parse.settings')
    # crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    # crawl_proc.crawl(HeadHunterSpider)
    # crawl_proc.crawl(AutoyoulaSpider)
    crawl_proc.crawl(InstagramSpider, login=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    crawl_proc.start()
