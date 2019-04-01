import requests
url = 'http://www.amaze.cn/productsdetails.aspx?id=39'
try:
    kv = {'user-agent': 'Chrome/73.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
    print(r.request.headers)
except:
    print('爬取失败')
