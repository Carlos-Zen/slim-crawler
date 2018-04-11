# coding:utf-8
# 爬虫应用入口
from proxy import *
from serialize import *
from base.spider import Spider
from bs4 import BeautifulSoup
import threading
import random
import requests
import time

proxy = get_proxies()

class SpiderMogo(Spider):
    base_url = 'http://sh.baletu.com/zhaofang/'
    debug = True

    def crawl_url(self):
        urls = []
        html = requests.get(self.base_url, headers=headers, timeout=20).text
        item_list = BeautifulSoup(html, 'lxml').find_all(
            'li', {'class': 'PBA_list_house'})
        for item in item_list:
            urls.append(''.join(['',item.find('a').get('href')]))
        return urls

    def crawl(self,html_doc):
        disposals = []
        info = SerializeBlt(html_doc).get()
        if self.debug:
            print(info)
        with open('data/result.txt', 'a') as f:
            f.write(info.json() + '\n')

SpiderMogo().run()