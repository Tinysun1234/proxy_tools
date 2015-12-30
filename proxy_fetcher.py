# -*- coding:utf8 -*-
'''
Created on Dec 29, 2015

@author: tisun
'''
import urllib2
import random 
import settings
from lxml.html import soupparser 

class ProxyFetcher(object):
    '''
    Fetch proxies from proxy websites
    '''

    websites_url = {'xici':'http://www.xicidaili.com/nn/'}
    proxies = []
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def fetch_xici(self):
        '''
        www.xicidaili.com/nn/ first page
        '''
        self.opener = urllib2.build_opener()
        ua = [('User-Agent', random.choice(settings.USER_AGENTS))]
        self.opener.addheaders = ua
        try:
            page = self.opener.open(self.websites_url['xici']).read()
            doc = soupparser.fromstring(page)
            proxy_sels = doc.xpath('//table[@id="ip_list"]//tr')
            for proxy_sel in proxy_sels[1:-1]:
                params = proxy_sel.xpath('./td')
#                 print params
                proxy = dict()
                proxy['ip'] = params[2].xpath('./text()')[0]
                proxy['port'] = params[3].xpath('./text()')[0]
                proxy['type'] = params[6].xpath('./text()')[0]
                self.proxies.append(proxy)
        except urllib2.URLError as e :
            print e

if __name__ == "__main__":
    proxy_fetcher = ProxyFetcher()
    proxy_fetcher.fetch_xici()
    print proxy_fetcher.proxies
