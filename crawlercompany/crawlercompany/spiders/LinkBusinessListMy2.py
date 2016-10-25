from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy


class CategoryBusinessListMyItem(Item):
    companyName = Field()
    companyAddress = Field()
    companyPhone = Field()
    category = Field()


class BusinessListMySpider(scrapy.Spider):
    name = "list-my"
    allowed_domains = ["businesslist.my"]
    start_urls = [
        'http://www.businesslist.my/category/general-business',
    ]

    def parse(self, response):
        url = Selector(response)
        try:
            totalPage = url.xpath(
                ".//*[@id='listings_left']/div[24]/a[3]/text()").extract()
            totalPageValue = totalPage[0].strip() if totalPage  else ''
            totals = int(totalPageValue) + 1
            for total in xrange(1, totals):
                crawlUrl = response.url + "/" + str(total)
                yield Request(url=crawlUrl, callback=self.ParseAllLinks, dont_filter=True)
                with open('text0.txt', 'a') as f:
                    f.write('{0}\n'.format(crawlUrl))

        except:
            pass

    def ParseAllLinks(self, response):
        url = Selector(response)

        urlElements = url.xpath(".//*[@id]/h4")
        for urlElement in urlElements:
            finalURLPage = urlElement.xpath(".//a/@href").extract()
            finalURLPage = finalURLPage[0].strip() if finalURLPage  else ''
            finalURLPage = 'http://www.businesslist.my' + finalURLPage
            with open('text1.txt', 'a') as f:
                f.write('{0}\n'.format(finalURLPage))
            yield Request(url=finalURLPage, callback=self.ParseDataCompany, dont_filter=True)

    def ParseDataCompany(self, response):
        url = Selector(response)
        companyName = url.xpath('//*[@id="company_name"]/text()').extract()
        companyName = companyName[0].strip() if companyName else ''
        companyAddress = url.xpath('string(//*[@id="company_details"]/div[2]/div[2])').extract()
        companyAddress = companyAddress[0].strip() if companyAddress else ''
        companyPhone = url.xpath('//*[@id="company_details"]/div[3]/div[2]/text()').extract()
        companyPhone = companyPhone[0].strip() if companyPhone else ''
        category = 'General Business'

        with open('my-company.txt', 'a') as f:
            f.write('{0};{1};{2};{3}\n'.format(category,
                                               companyName,
                                               companyAddress,
                                               companyPhone))



