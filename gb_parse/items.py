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


class InstagramTagItem(scrapy.Item):
    _id = scrapy.Field()
    instagram_id = scrapy.Field()
    name = scrapy.Field()
    picture_url = scrapy.Field()
    image_info = scrapy.Field()


class InstagramPostItem(scrapy.Item):
    _id = scrapy.Field()
    data = scrapy.Field()
    picture_url = scrapy.Field()
    date_parse = scrapy.Field()
    image_info = scrapy.Field()


class InstagramUserItem(scrapy.Item):
    _id = scrapy.Field()
    data = scrapy.Field()
    date_parse = scrapy.Field()


class InstagramUserFollowingItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    following_user_id = scrapy.Field()


class InstagramUserFollowedByItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    followed_by_user_id = scrapy.Field()
