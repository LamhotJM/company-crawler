# -*- coding: utf-8 -*-

# Scrapy settings for crawlercompany project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import string
import random
BOT_NAME = 'crawlercompany'

SPIDER_MODULES = ['crawlercompany.spiders']
NEWSPIDER_MODULE = 'crawlercompany.spiders'


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))


USER_AGENT = "(+lamhot" +id_generator(1000, '2636612356265136793YUIO')

JavaScript_Enabled=	"Yes"

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

PROXY_LIST = 'list.txt'

headers={'User-Agent': 'Mozilla/5.0'}

SPIDER_MIDDLEWARES = {
}

RETRY_TIMES = 10

RETRY_HTTP_CODES = [500, 302,502, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
   'crawlercompany.middlewares.ProxyMiddleware': 543,
}

http_proxy='http_proxy=http://lamhot:PASSWORD@fr.proxymesh.com:31280'

PROXIES = [
  {'ip_port': '47.88.3.97:9398', 'user_pass': ''},
  {'ip_port': '47.88.26.105:9398', 'user_pass': ''},
  {'ip_port': '47.88.7.56:9398','user_pass': ''},
  {'ip_port': '47.88.7.62:9398','user_pass': ''},
  {'ip_port': '47.88.6.231:9398','user_pass': ''},
  {'ip_port': '47.88.7.9:9398','user_pass': ''},
  {'ip_port': '47.88.6.172:9398','user_pass': ''},
]

DOWNLOAD_DELAY =10

AUTOTHROTTLE_MAX_DELAY = 60
