# -*- coding: utf-8 -*-
import scrapy
import logging
import time
import re

from scrapy.selector import Selector
from scrapy.http import Request

from bs4 import BeautifulSoup


class YellowPageIdSpider(scrapy.Spider):
    name = "ypid"
    allowed_domains = ["yellowpages.co.id"]
    start_urls = [
        'https://www.yellowpages.co.id/category/industry',
        'https://www.yellowpages.co.id/category/restaurant',
        'https://www.yellowpages.co.id/category/transportation',
        'https://www.yellowpages.co.id/category/travel',
        'https://www.yellowpages.co.id/category/automotive',
        'https://www.yellowpages.co.id/category/chemical',
        'https://www.yellowpages.co.id/category/computer',
        'https://www.yellowpages.co.id/category/education',
        'https://www.yellowpages.co.id/category/electronic',
        'https://www.yellowpages.co.id/category/finance',
        'https://www.yellowpages.co.id/category/hotel',
        'https://www.yellowpages.co.id/category/property',
    ]

    def parse(self, response):
        # Parse the current page
        YellowPageIdSpider.ParsePagination(response)
        time.sleep(2)

        current_page = YellowPageIdSpider.extract_current_page_from_link(response.url)
        logging.debug("Current page %s" % current_page)
        # Find next page if possible
        soup = BeautifulSoup(response.text, 'html.parser')
        next_page_link = soup.find('a', href=True, text=str(current_page + 1))

        if not next_page_link:
            next_page_link = soup.find('a', href=True, text=re.compile('.*Next.*'))

        logging.debug("Next page %s" % next_page_link)
        if next_page_link:
            url_request = "https://www.yellowpages.co.id"+next_page_link.get('href')
            logging.debug("Add link to queue %s" % url_request)
            yield Request(url=url_request, callback=self.parse, dont_filter=True)

    @staticmethod
    def extract_current_page_from_link(url):
        if url.endswith(''):
            page = url[url.rfind('=') + 1:]
            try:
                page_number = int(page)
            except ValueError:
                page_number = 1
        return page_number

    @staticmethod
    def ParsePagination(response):
        url = Selector(response)

        elements = url.xpath('//*/div[1]/div[3]/div[2]/div[3]/div/div[1]/div/div/div')
        # logging.debug(elements.extract())
        for element in elements:
            companyName = element.xpath(".//*/div/div/h4/a/text()").extract()
            companyName = companyName[0].strip() if companyName else ''
            companyAddress1 = element.xpath(".//*/div[2]/div/span/text()").extract()
            companyAddress1 = companyAddress1[0].strip() if companyAddress1 else ''
            companyAddress2 = element.xpath(".//*/div[3]/div/span/text()").extract()
            companyAddress2 = companyAddress2[0].strip() if companyAddress2 else ''
            companyAddress3 = element.xpath(".//*/div[4]/div/span/text()").extract()
            companyAddress3 = companyAddress3[0].strip() if companyAddress3 else ''
            companyEmail = element.xpath(".//*/div/div/a[2]/@href").extract()
            companyEmail = companyEmail[0].strip() if companyEmail else ''
            companyEmail = companyEmail.replace("mailto:", "")
            category = element.xpath(".//*/div/div/span/strong/a/text()").extract()
            category = category[0].strip() if category else ''

            companyAddress = companyAddress1.replace("\n", " ") + ", " + companyAddress2.replace("\n",
                                                                                                 " ") + ", " + companyAddress3.replace(
                "\n", " ")
            companyAddress = re.sub(r"(?<=[a-z])\r?\n", " ", companyAddress)
            logging.debug("Name %s " % companyName)
            logging.debug("Addess %s" % companyAddress)
            logging.debug("Emil %s" % companyEmail)
            logging.debug("Cat %s" % category)
            with open('ypi.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAddress, companyEmail, category))

                # catList = {'automotive','industrial','business', 'medical','restaurant','/'}
                #  for category in catList:
                #       crawlUrl = (proviceLink + category)
                #        yield Request(url=crawlUrl, callback=self.ParseSubCat, dont_filter=True)
