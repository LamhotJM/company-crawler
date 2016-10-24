# -*- coding: utf-8 -*-

import random
from settings import PROXIES
from settings import http_proxy
import base64
class ProxyMiddleware(object):
    #def process_request(self, request, spider):
     #   request.meta['proxy'] = http_proxy
        # overwrite process request


    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://fr.proxymesh.com:31280"
        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "lamhot:test123@Test"
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
