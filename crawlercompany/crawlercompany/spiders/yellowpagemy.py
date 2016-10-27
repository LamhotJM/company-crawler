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
        'https://www.yellowpages.my/listing/allcategories.php',
    ]

    def parse(self,response,):
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
