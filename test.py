#coding:utf-8
#

import requests

r = requests.get('http://wkporttest.9fbank.com/amity/wkamity/getSecretkeys?parterId=5202248910&secretKey=luamvqfi6171219095100377j6zphtu3&visitTime=1',proxies={'http':"http://127.0.0.1:8888"})
print(r.content)