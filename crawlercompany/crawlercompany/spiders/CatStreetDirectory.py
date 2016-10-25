from scrapy.selector import Selector
import scrapy
import logging
from scrapy.item import Field, Item


class MalayItem(Item):
    companyName = Field()
    companyAddress = Field()
    companyPhone = Field()
    category = Field()


class DirectorySpider(scrapy.Spider):
    name = "csd"
    allowed_domains = ["streetdirectory.com.my"]
    start_urls = [
        'http://www.streetdirectory.com.my/businessfinder/malaysia/kl/company/1099/Foot_Reflexology/',
    ]

    def parse(self, response):
        from scrapy.selector import HtmlXPathSelector
        hxs = Selector(response)
       # element = hxs.select

        #url = Selector(response)
        #responds = response.body_as_unicode()
        #body = str(responds)
        #url= Selector(text=body)
        #logging.debug(body)

        import time
        time.sleep(4)
                             #.//*[@id='listing_category_content']/tbody/tr/td/div/div/table/tbody

        elements = hxs.xpath(".//*[@id='listing_category_content']//tr/td/div/div/table")
        for element in elements:
            companyName = element.xpath(".//tr[1]/td[3]/div/h3/a/text()").extract()
            companyName = companyName[0].strip() if companyName  else ''
            companyAdress = element.xpath('.//tr[2]/td/table//tr[@id="tr_address"]/td[3]/text()').extract()
            companyAdress = companyAdress[0].strip() if companyAdress else ''
            companyPhone = element.xpath('.//*[@itemprop="telephone"]/text()').extract()
            companyPhone = companyPhone[0].strip() if companyPhone else ''
            companyCategory = element.xpath(
                './/tr[2]/td/table//tr[@id="listing_tr_category"]/td[3]/a/text()').extract()
            companyCategory = companyCategory[0].strip() if companyCategory else ''

            with open('sd3.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAdress, companyPhone, companyCategory))
