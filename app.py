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

class Spider58(Spider):

    def crawl_url(self):
        url = []
        for line in open('result/租房_urls.txt', 'r'):
            url.append(line.replace('\n', ''))
        return url

    def crawl(self,html_doc):
        disposals = []
        info = HouseSerialize(html_doc).get()
        with open('result/result.txt', 'a') as f:
            f.write(info.json() + '\n')

    # def get_data_from_url(self,url):
    #     while True:
    #         # proxies = proxy[random.randint(0,len(proxy)-1)]
    #         try:
    #             html = requests.get(url, headers=headers,#proxies=proxies,
    #                                 timeout=5).text
    #             print(html)
    #             if '访问过于频繁，本次访问做以下验证码校验' in html:
    #                 pass
    #         except Exception as e:
    #             print(e)
    #             continue

    #     basic_item = BeautifulSoup(html, 'lxml')
    #     info = self.get_fields_from_content(basic_item)
    #     with open('result/result.txt', 'a') as f:
    #         f.write(info.json() + '\n')    


Spider58().run()