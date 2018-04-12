#coding:utf-8
#

import requests
from base.dict import *
from base.log import *
from proxy import *

url = 'http://control.uuzu.com/api/game?company_id=1&platform_id=2&page=1&per_page=10'
resp = requests.get(url, headers=headers,#proxies=proxies,
                                    timeout=5)
print(resp)
