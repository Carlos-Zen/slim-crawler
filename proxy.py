import redis

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

key = "useful_proxy"
host = "10.18.98.134"
port = 6379
def get_proxies():
    conn = redis.Redis(host=host, port=port, db=0)
    item_dict = conn.hgetall(key)
    return [{'http':''.join(['http://',key.decode('utf8')])} for key,item in item_dict.items()]

def delete_proxies():
    conn = redis.Redis(host=host, port=port, db=0)
    conn.hdel(key,'*')

if __name__ == '__main__':
    proxy=get_proxies()
    print(proxy)
