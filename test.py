#coding:utf-8
#
from random import choice
import aiohttp
import asyncio
import async_timeout
from proxy import headers
from bs4 import BeautifulSoup as bs
import requests
# async def log(message):
contents = []
bad_url=[]
proxies = ['http://'+p for p in [
  "101.53.101.172:9999", 
  "101.71.226.135:9000", 
  "101.81.141.175:9999", 
  "103.232.147.16:1080", 
  "104.131.82.152:8080", 
  "110.137.115.128:8080", 
  "110.73.34.94:8123", 
  "112.21.164.58:1080", 
  "113.214.13.1:8000", 
  "113.218.219.195:28602", 
  "113.218.219.211:36996", 
  "114.214.164.38:9999", 
  "114.238.216.42:30754", 
  "114.99.73.252:43711", 
  "116.11.254.37:80", 
  "116.54.77.153:40271" ]]


def parse(contents):
	for c in contents:
		s = bs(c,'lxml')
		print(s.head)

async def wget(url):
	try:
		async with aiohttp.ClientSession() as session:
			async with async_timeout.timeout(5):
					async with session.get(url,headers=headers,proxy=choice(proxies)) as resp:
						content = await resp.read()
						contents.append(content)
	except Exception as e:
		bad_url.append(url)

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn','http://www.sina.com.cn']]
loop.run_until_complete(asyncio.wait(tasks))
parse(contents)
print(bad_url)
loop.close()