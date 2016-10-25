from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy


class MalayItem(Item):
    companyName = Field()
    companyAddress = Field()
    companyPhone = Field()
    category = Field()


class StreetDirectorySpider(scrapy.Spider):
    name = "sd"
    allowed_domains = ["streetdirectory.com.my"]
    start_urls = [
        'http://www.streetdirectory.com.my/businessfinder/malaysia/',
    ]

    def parse(self, response):
        url = Selector(response)
        try:
            elements = url.xpath('//*[@id="state_dipslay"]/div/a')
            for element in elements:
                proviceLink = element.xpath(".//@href").extract()
                proviceLink = proviceLink[0].strip() if proviceLink else ''
                catList = {'/', 'restaurant', 'industrial', 'business', 'medical', 'automotive'}
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
                if subCat=='javascript:void(0)':
                    pass
                else:
                    yield Request(url=subCat, callback=self.ParseSubCat, dont_filter=True)
                    with open('sd2.txt', 'a') as f:
                        f.write('{0}\n'.format(subCat))

        except:
            pass

    def ParseCategory(self, response):
        url = Selector(response)
        elements = url.xpath(".//*[@id='listing_category_content']/tbody/tr/td/div/div/table/tbody")
        for element in elements:
            companyName = element.xpath("string(.//tr[1]/td[3]/div/h3)").extract()
            companyName = companyName[0].strip() if companyName  else ''
            companyAdress = element.xpath('string(.//tr[2]/td/table/tbody/tr[@id="tr_address"]/td[3])').extract()
            companyAdress = companyAdress[0].strip() if companyAdress else ''
            companyPhone = element.xpath('string(.//tr[3]/td[3]/span)').extract()
            companyPhone = companyPhone[0].strip() if companyPhone else ''
            companyCategory = element.xpath('string(.//tr[2]/td/table/tbody/tr[@id="listing_tr_category"]/td[3])').extract()
            companyCategory = companyCategory[0].strip() if companyCategory else ''

            with open('sd3.txt', 'a') as f:
                f.write('{0};{1};{2};{3}\n'.format(companyName, companyAdress, companyPhone, companyCategory))

