import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time
import logging
import string

class YellowPageMyCategorySpider(scrapy.Spider):
    name = "category_ypmy"
    allowed_domains = ["yellowpages.my"]
    start_urls = [
        'http://www.yellowpages.my/listing/allcategories.php',
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1600, 1000)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)
        for count in xrange(26, 27):
            self.driver.find_element_by_xpath(
                ".//*[@id='page-top']/div/div[2]/div/div/a["+str(count)+"]").click()
            time.sleep(2)
            self.html = self.driver.page_source
            self.scraping()

        self.driver.quit()

    def scraping(self):
            time.sleep(2)
            elements=Selector(text=self.html).xpath(".//*[@id='browse_category_']/li")
            for element in elements:
                linkCategory = element.xpath(".//a/@href").extract()
                linkCategory = linkCategory[0].strip() if linkCategory else ''
                logging.debug(linkCategory)
                printable = set(string.printable)
                ##convert to ascii
                asciiResult = filter(lambda x: x in printable, linkCategory)
                with open('yellowpagemy-category.txt', 'a') as f:
                    f.write('{0}\n'.format(asciiResult))
