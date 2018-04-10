import redis

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"}

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
