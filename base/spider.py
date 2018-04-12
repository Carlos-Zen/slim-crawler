#coding:utf-8
import queue
from setting import *
import time
import random
import requests
from proxy import *
from bs4 import BeautifulSoup
from base.log import *
import time
from setting import *
from base.log import *

class Spider(object):
    """ The spider base class
    """
    def __init__(self):
        self.url_queue = queue.Queue()
        self.crawl_date = time.strftime("%Y-%m-%d", time.localtime()) 
        pass

    def run(self):
        for url in self.crawl_url():
            self.url_queue.put(url)
        self._crawl_queue()

    def crawl_url(self):
        """Need to be implemented by son classes.

        Returns:
            Url list will return for spider to crawl.
            It will used as Queue.
        """
        return []

    def _crawl_queue(self):
        while not self.url_queue.empty():
            url = self.url_queue.get()
            logger.info('Crapy: '+url)
            headers['Referer'] = self.base_url
            try:
                resp = requests.get(url, headers=headers,#proxies=proxies,
                                    timeout=5)
            except Exception as e:
                logger.error('request %s failed.reason:%s' % (url,e))
            resp.encoding = 'utf-8'
            html = resp.text
            basic_item = BeautifulSoup(html, 'lxml')
            self.crawl(basic_item)
            time.sleep(random.random())
            if DEBUG:
                break

    def crawl(self,url):
        """Implemented by son classes.
        """
        pass
