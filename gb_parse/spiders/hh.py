import scrapy
from ..loaders import HeadHunterJobLoader, HeadHunterCompanyLoader


class HeadHunterSpider(scrapy.Spider):
    name = 'headhunter'
    allowed_domains = ['hh.ru']
    start_url = 'https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113'

    page_xpath = {
        'pagination': '//span/a[@class="bloko-button HH-Pager-Control"]/@href',
        'job_urls': '//span[@class="g-user-content"]/a/@href',
    }

    job_xpath = {
        "job_name": '//div[@class="vacancy-title"]/h1//text()',
        "salary": '//div[@class="vacancy-title"]/p[@class="vacancy-salary"]//text()',
        "job_description": '//div[@class="g-user-content"][@data-qa="vacancy-description"]//text()',
        "skills": '//span[@class="bloko-tag__section bloko-tag__section_text"][@data-qa="bloko-tag__text"]/text()',
        "company_url": '//div[@class="vacancy-company__details"]/a[@class="vacancy-company-name"]/@href',
    }

    company_xpath = {
        'company_name': '//h1[@class="bloko-header-1"][@data-qa="bloko-header-1"]//text()',
        'company_website': '//a[@data-qa="sidebar-company-site"]/@href',
        'company_scope': '//div[@class="employer-sidebar-block"]/div[@data-qa="sidebar-header-color"]/../p/text()',
        'company_description': '//div[@class="company-description"]//text()',
        'company_jobs_page_url': '//a[@data-qa="employer-page__employer-vacancies-link"]/@href',
    }

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.parse)

    def parse(self, response, **kwargs):
        for job_page in response.xpath(self.page_xpath['job_urls']):
            yield response.follow(job_page, callback=self.job_page_parse)

        for pag_page in response.xpath(self.page_xpath['pagination']):
            yield response.follow(pag_page, callback=self.parse)

    def job_page_parse(self, response, **kwargs):
        loader = HeadHunterJobLoader(response=response)
        loader.add_value('job_url', response.url)
        for name, selector in self.job_xpath.items():
            loader.add_xpath(name, selector)
        item = loader.load_item()
        company_page = response.xpath(self.job_xpath['company_url']).get()

        yield item
        yield response.follow(company_page, callback=self.company_page_parse)

    def company_page_parse(self, response, **kwargs):
        loader = HeadHunterCompanyLoader(response=response)
        loader.add_value('company_url', response.url)
        for name, selector in self.company_xpath.items():
            loader.add_xpath(name, selector)
        item = loader.load_item()
        company_jobs = response.xpath(self.company_xpath['company_jobs_page_url']).get()

        yield item
        yield response.follow(company_jobs, callback=self.parse)
