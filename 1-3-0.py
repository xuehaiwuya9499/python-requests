import requests
keyword = 'Python'
try:
    kv = {'wd': keyword}
    r = requests.get('http://www.baidu.com/s', params=kv)
    print(r.request.url)
    print(r.status_code)
    r.raise_for_status()
    print(r.text)
except:
    print('爬取失败！')
