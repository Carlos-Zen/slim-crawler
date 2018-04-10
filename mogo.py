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
    base_url = 'http://zz.mogoroom.com'
    base_url = 'http://zz.mogoroom.com/list'

    def crawl_url(self):
        urls = []
        html = requests.get(page_url, headers=headers, timeout=20).text
        item_list = BeautifulSoup(html, 'lxml').find_all(
            'div', {'class': 'item-room'})
        if item_list == []:
            break
        for item in item_list:
            urls.append(''.join([self.base_url,item.find('a').get('href')]))
        return urls

    def crawl(self,html_doc):
        disposals = []
        info = HouseSerialize(html_doc).get()
        with open('result/result.txt', 'a') as f:
            f.write(info.json() + '\n')

SpiderMogo().run()