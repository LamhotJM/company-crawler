from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy


class CategoryBusinessListMyItem(Item):
    url_cat = Field()


class CategoryBusinessListMySpider(scrapy.Spider):
    name = "category"
    allowed_domains = ["businesslist.my"]
    start_urls = [
        'http://www.businesslist.my/browse-business-directory',
    ]

    def parse(self, response):
        url = Selector(response)
        rootElement = url.xpath(".//*[@id='right']/ul/li")
        for subRoot in rootElement:
            url_cat = subRoot.xpath(
                ".//a/@href").extract()
            url_cat = url_cat[0].strip() if url_cat  else ''
            url_cat = 'http://www.businesslist.my' + url_cat
            yield Request(url=url_cat, callback=self.ParseTotalPage, dont_filter=True)

    def ParseTotalPage(self, response):
        url = Selector(response)
        try:
            totalPage = url.xpath(
                ".//*[@id='listings_left']/div[24]/a[3]/text()").extract()
            totalPageValue = totalPage[0].strip() if totalPage  else ''

            with open('url-cat-total-page.txt', 'a') as f:
                f.write('{0};{1}\n'.format(response.url, totalPageValue))
        except:
            pass



