import re
from scrapy import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from .items import AutoYoulaItem, HeadHunterJobItem, HeadHunterCompanyItem
from urllib.parse import urljoin


def get_autor(js_string):
    re_str = re.compile(r"youlaId%22%2C%22([0-9|a-zA-Z]+)%22%2C%22avatar")
    result = re.findall(re_str, js_string)
    return f'https://youla.ru/user/{result[0]}' if result else None


def get_specifications(itm):
    tag = Selector(text=itm)
    result = {tag.css('.AdvertSpecs_label__2JHnS::text').get(): tag.css(
        '.AdvertSpecs_data__xK2Qx::text').get() or tag.css('a::text').get()}
    return result


def specifications_out(data: list):
    result = {}
    for itm in data:
        result.update(itm)
    return result


def get_full_url(url):
    return urljoin('https://hh.ru/', url)


def get_company(seq: list):
    seen = set()
    seen_add = seen.add
    str_ = ' '.join([x for x in seq if not (x in seen or seen_add(x))])
    return str_.replace('\xa0', '').strip()


class AutoYoulaLoader(ItemLoader):
    default_item_class = AutoYoulaItem
    title_out = TakeFirst()
    url_out = TakeFirst()
    description_out = TakeFirst()
    autor_in = MapCompose(get_autor)
    autor_out = TakeFirst()
    specifications_in = MapCompose(get_specifications)
    specifications_out = specifications_out


class HeadHunterJobLoader(ItemLoader):
    default_item_class = HeadHunterJobItem
    job_url_out = TakeFirst()
    job_name_out = TakeFirst()
    salary_in = ''.join
    salary_out = TakeFirst()
    job_description_in = ''.join
    job_description_out = TakeFirst()
    company_url_in = MapCompose(get_full_url)
    company_url_out = TakeFirst()


class HeadHunterCompanyLoader(ItemLoader):
    default_item_class = HeadHunterCompanyItem
    company_url_out = TakeFirst()
    company_name_out = get_company
    company_website_out = TakeFirst()
    company_description_in = ''.join
    company_description_out = TakeFirst()
    company_jobs_page_url_out = TakeFirst()
