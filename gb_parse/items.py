# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GbParseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AutoYoulaItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    autor = scrapy.Field()
    specifications = scrapy.Field()


class HeadHunterJobItem(scrapy.Item):
    _id = scrapy.Field()
    job_url = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    job_description = scrapy.Field()
    skills = scrapy.Field()
    company_url = scrapy.Field()


class HeadHunterCompanyItem(scrapy.Item):
    _id = scrapy.Field()
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    company_website = scrapy.Field()
    company_scope = scrapy.Field()
    company_description = scrapy.Field()
    company_jobs_page_url = scrapy.Field()
    company_jobs = scrapy.Field()
