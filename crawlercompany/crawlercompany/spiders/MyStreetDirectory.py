import scrapy
import logging
import time
import re

from scrapy.selector import Selector
from scrapy.http import Request

from bs4 import BeautifulSoup


class StreetDirectorySpider(scrapy.Spider):
    name = "my_sd"
    allowed_domains = ["streetdirectory.com.my"]
    start_urls = [
        'http://www.streetdirectory.com.my/businessfinder/malaysia/'
    ]

    def parse(self, response):
        url = Selector(response)
        try:
            elements = url.xpath('//*[@id="state_dipslay"]/div/a')
            for element in elements:
                proviceLink = element.xpath(".//@href").extract()
                proviceLink = proviceLink[0].strip() if proviceLink else ''
                catList = {'automotive','industrial','business', 'medical','restaurant','/'}
                for category in catList:
                    crawlUrl = (proviceLink + category)
                    yield Request(url=crawlUrl, callback=self.ParseSubCat, dont_filter=True)
                    with open('sd1.txt', 'a') as f:
                        f.write('{0}\n'.format(crawlUrl))

        except:
            pass

    def ParseSubCat(self, response):
        url = Selector(response)
        try:
            elements = url.xpath(
                ".//*[@id='main_page_content']/table//tr/td/table//tr/td/table//tr/td|//tr/td/div/div/div/a")
            for element in elements:
                subCat = element.xpath(".//@href").extract()
                subCat = subCat[0].strip() if subCat  else ''
                logging.debug(subCat)
                yield Request(url=subCat, callback=self.ParseCategory, dont_filter=True)

        except:
            pass

    def ParseCategory(self, response):
        StreetDirectorySpider.ParsePagination(response)
        time.sleep(2)

        current_page = StreetDirectorySpider.extract_current_page_from_link(response.url)
        logging.debug("Current page %s" % current_page)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_page_link = soup.find('a', href=True, text=str(current_page + 1))

        if not next_page_link:
            next_page_link = soup.find('a', href=True, text=re.compile('.*Next.*'))

        logging.debug("Next page %s" % next_page_link)
        if next_page_link:
            url_request = next_page_link.get('href')
            logging.debug("Add link to queue %s" % url_request)
            yield Request(url=url_request, callback=self.parse, dont_filter=True)

    @staticmethod
    def extract_current_page_from_link(url):
        if url.endswith('/'):
            url = url[0:len(url) - 1]
            page = url[url.rfind('/') + 1:]
            try:
                page_number = int(page)
            except ValueError:
                page_number = 1
        return page_number

    @staticmethod
    def ParsePagination(response):
        url = Selector(response)
        time.sleep(2)
        elements = url.xpath(".//*[@id='listing_category_content']//tr/td/div/div/table")
        for element in elements:
            companyName = element.xpath(".//tr[1]/td[3]/div/h3/a/text()|.//tr/td/div/h3/a/text()").extract()
            companyName = companyName[0].strip() if companyName  else ''
            companyAdress = element.xpath('.//tr[2]/td/table//tr[@id="tr_address"]/td[3]/text()').extract()
            companyAdress = companyAdress[0].strip() if companyAdress else ''
            companyPhone = element.xpath('.//*[@itemprop="telephone"]/text()').extract()
            companyPhone = companyPhone[0].strip() if companyPhone else ''
            companyCategory = element.xpath(
                './/tr[2]/td/table//tr[@id="listing_tr_category"]/td[3]/a/text()|.//a/b/text()').extract()
            companyCategory = companyCategory[0].strip() if companyCategory else ''

            with open('sd_my.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAdress, companyPhone, companyCategory))
