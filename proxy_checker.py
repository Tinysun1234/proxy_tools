# -*- coding : utf8 -*-
'''
Created on Dec 29, 2015

@author: tisun
'''

import urllib2
from time import time
from proxy_fetcher import ProxyFetcher

class ProxyChecker(object):
    '''
    proxy checker class
    '''
    unchecked_proxies = [{'type':'http', 'ip':'123.95.128.65', 'port':'8123'},
                           {'type':'http', 'ip':'117.136.234.9', 'port':'80'}
                           ]
    available_proxies = []
    unavailable_proxies = []
    
    test_url = 'http://www.baidu.com'
    max_wait_time = 3

    def __init__(self, proxies):
        '''
        Constructor
        '''
        if proxies:
            self.unchecked_proxies = proxies
        pass
    
    def check_proxies(self):
        '''
        check all unchecked proxies
        '''
        for proxy in self.unchecked_proxies:
            self.check_one_proxy(proxy)
    
    def check_one_proxy(self, proxy):
        '''
        check if the proxy is available
        '''
        proxy_handler = urllib2.ProxyHandler({proxy['type']:'%s:%s' % (proxy['ip'], proxy['port'])})
        opener = urllib2.build_opener(proxy_handler)
        try:
            t_start = time()
            resp = opener.open(self.test_url, timeout=self.max_wait_time).read()
            t_use = time() - t_start
            if 'javascript' in resp:
                print 'Proxy %s-%s:%s is Available! Latecy is %us!' % (proxy['type'], proxy['ip'], proxy['port'], t_use)
                proxy['latency'] = t_use
                self.available_proxies.append(proxy)
            else:
                print 'Proxy %s-%s:%s is Unavailable!' % (proxy['type'], proxy['ip'], proxy['port'])
                self.unavailable_proxies.append(proxy)
            
        except urllib2.URLError as e :
            print e
    
    
if __name__ == '__main__':
    pf = ProxyFetcher()
    pf.fetch_xici()
    pc = ProxyChecker(pf.proxies)
    pc.check_proxies()    
