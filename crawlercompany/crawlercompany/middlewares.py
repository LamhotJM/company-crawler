# -*- coding: utf-8 -*-

import random
from settings import PROXIES
from settings import http_proxy
import base64
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % proxy['ip_port']

    #def process_request(self, request, spider):
        # Set the location of the proxy
     #   request.meta['proxy'] = "http://fr.proxymesh.com:31280"
        # Use the following lines if your proxy requires authentication
      #  proxy_user_pass = "lamhot:test123@Test"
        # setup basic authentication for the proxy
       # encoded_user_pass = base64.encodestring(proxy_user_pass)
       # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

class ProxyMeshMiddleware(object):
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://paygo.crawlera.com:8010"
        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "rcouraud:FEf3zwVsNz"
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

        #HTTP_PROXY = 'http://lamhot:test123@Test@fr.proxymesh.com:31280'
        #request.meta['proxy'] = HTTP_PROXY