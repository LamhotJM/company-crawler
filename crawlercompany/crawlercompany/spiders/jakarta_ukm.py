# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy
import string


class JakartaUKMItem(Item):
    companyName = Field()
    companyAddress = Field()
    companyContact = Field()
    product = Field()


class JakartaUKMSpider(scrapy.Spider):
    name = "umkjakarta"
    allowed_domains = ["jakarta.go.id"]
    start_urls = [
        'http://bidangukmdki.jakarta.go.id/new/index.php/ukm/data/',
    ]

    def parse(self, response):
        for i in range(0, 1199):
            i = i * 15
            crawlUrl = response.url + str(i)
            yield Request(url=crawlUrl, callback=self.parse_pagination, dont_filter=True)

    def parse_pagination(self, response):
        url = Selector(response)
        mother = url.xpath(".//body/div/table/tbody")
        for i in mother:
            try:
                companyName = i.xpath(".//tr/td[2]/b/text()|.//tr/td[2]/a/b/text()").extract()
                companyName = companyName[0].strip() if companyName else ''
                companyAddressContact = i.xpath(".//tr/td[2]/div/text()").extract()
                printable = set(string.printable)
                companyAddress1 = companyAddressContact[0].strip() if companyAddressContact[0] else ''
                companyAddress1 = filter(lambda x: x in printable, companyAddress1)
                companyAddress2 = companyAddressContact[1].strip() if companyAddressContact[1] else ''
                companyAddress2 = filter(lambda x: x in printable, companyAddress2)
                companyAddress3 = companyAddressContact[2].strip() if companyAddressContact[2] else ''
                companyAddress3 = filter(lambda x: x in printable, companyAddress3)
                companyContact = companyAddressContact[3].strip() if companyAddressContact[3] else ''
                companyContact = filter(lambda x: x in printable, companyContact)
                companyAddress = companyAddress1.replace("\n", " ") + ", " + companyAddress2.replace("\n",
                                                                                                     " ") + ", " + companyAddress3.replace(
                    "\n", " ")
                product = i.xpath(".//tr/td[3]/div/text()").extract()
                product = product[0].strip() if product  else ''
                item = JakartaUKMItem(companyName=companyName,
                                      companyAddress=" ".join(companyAddress.split()),
                                      companyContact=companyContact.replace("\n", " "),
                                      product=product, )

                with open('ukm-jakarta.txt', 'a') as f:
                    f.write('{0};{1};{2};{3}\n'.format(item['companyName'],
                                                       item['companyAddress'],
                                                       item['companyContact'],
                                                       item['product']))
            except:
                pass
