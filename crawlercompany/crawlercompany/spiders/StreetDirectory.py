from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy
import time


class MalayItem(Item):
    companyName = Field()
    companyAddress = Field()
    companyPhone = Field()
    category = Field()


class StreetDirectorySpider(scrapy.Spider):
    name = "sd"
    allowed_domains = ["streetdirectory.com.my"]
    start_urls = [
        'http://www.streetdirectory.com.my/businessfinder/indonesia/'
        '',
    ]

    def parse(self, response):
        url = Selector(response)
        try:
            elements = url.xpath('//*[@id="state_dipslay"]/div/a')
            for element in elements:
                proviceLink = element.xpath(".//@href").extract()
                proviceLink = proviceLink[0].strip() if proviceLink else ''
                catList = {'automotive','industrial','business', 'medical', 'restaurant','/'}
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
                ".//*[@id='main_page_content']/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td|//tr/td/div/div/div/a")
            for element in elements:
                subCat = element.xpath(".//a/href|.//@href").extract()
                subCat = subCat[0].strip() if subCat  else ''
                if subCat == 'javascript:void(0)':
                    pass
                else:
                    yield Request(url=subCat, callback=self.ParseCategory, dont_filter=True)
                    with open('sd2.txt', 'a') as f:
                        f.write('{0}\n'.format(subCat))

        except:
            pass

    def ParseCategory(self, response):
        hxs = Selector(response)
        pageElement = 1
        pageNumber = 1

        while True:
            time.sleep(2)
            text = hxs.xpath('//*[@id="paging"]/div/form/table//tr/td/span/span/span[' + str(
                pageElement) + ']')

            urlRequest = response.url + 'All/' + str(pageNumber)
            yield Request(url=urlRequest, callback=self.ParsePagination, dont_filter=True)

            pageElement = pageElement + 1
            pageNumber = pageNumber + 1
            if pageNumber % 9 == 0:
                pageElement = 4

            if text.extract() == []:
                break

    def ParsePagination(self, response):
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

            with open('sd_id.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAdress, companyPhone, companyCategory))
