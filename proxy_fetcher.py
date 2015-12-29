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
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def fetch_xici(self):
        '''
        www.xicidaili.com/nn/    高匿代理
        '''
        self.opener = urllib2.build_opener()
        ua = [('User-Agent', random.choice(settings.USER_AGENTS))]
        self.opener.addheaders = ua
        try:
            page = self.opener.open(self.websites_url['xici']).read()
            doc = soupparser.fromstring(page)
        except urllib2.URLError as e :
            print e
