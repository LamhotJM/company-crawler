# -*- coding: utf-8 -*-
import scrapy
import logging
import time
import re

from scrapy.selector import Selector
from scrapy.http import Request

from bs4 import BeautifulSoup


class YellowPageMySpider(scrapy.Spider):
    name = "ypmy2"
    allowed_domains = ["yellowpages.my"]
    start_urls = [
        'http://www.yellowpages.my/listing/guide/cafes']

    def parse(self, response):
        # Parse the current page
        YellowPageMySpider.ParsePagination(response)
        time.sleep(2)

        current_page = YellowPageMySpider.extract_current_page_from_link(response.url)
        logging.debug("Current page %s" % current_page)
        # Find next page if possible
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
        if url.endswith(''):
            page = url[url.rfind('/') + 1:]
            try:
                page_number = int(page)
            except ValueError:
                page_number = 1
        return page_number

    @staticmethod
    def ParsePagination(response):
        url = Selector(response)
        elements = url.xpath(".//*/ul/li/div[2]")
        for element in elements:
            companyName = element.xpath(".//div[1]/text()|.//div[1]/a/text()").extract()
            try:
                companyName = companyName[1].strip() if companyName else ''
            except:
                companyName = companyName[0].strip() if companyName else ''

            companyAddress = element.xpath('.//div[2]/text()').extract()
            try:
                companyAddress = companyAddress[1].strip()if companyAddress else ''
            except:
                companyAddress = companyAddress[0].strip() if companyAddress else ''

            if not companyAddress:
                companyAddress = element.xpath('.//div[3]/text()').extract()
                try:
                    companyAddress = companyAddress[1].strip() if companyAddress else ''
                except:
                    companyAddress = companyAddress[0].strip() if companyAddress else ''

            companyPhone = element.xpath(".//div/span/@data-content").extract()
            companyPhone = companyPhone[0].strip() if companyPhone else ''
            companyPhone=companyPhone.replace("<a href='tel:", "")
            companyPhone = companyPhone.split("'>")
            category = element.xpath('.//div[2]/a/text()').extract()
            try:
                category= category[1].strip() if category else ''
            except:
                category = category[0].strip() if category else ''

            if not category:
                category = element.xpath('.//div[3]/a/text()').extract()
                try:
                    category = category[1].strip() if category else ''
                except:
                    category = category[0].strip() if category else ''

            logging.debug("Name %s " % companyName)
            logging.debug("Addess %s" % companyAddress)
            logging.debug("Phone %s" % companyPhone[0])
            logging.debug("Category %s" % category)
            with open('ypmy.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAddress, companyPhone[0], category))



