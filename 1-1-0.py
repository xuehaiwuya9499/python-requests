import requests
url = 'http://www.ngchina.com.cn/'
try:
    r = requests.get(url)
    print(r.request.headers)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print('爬取失败！')
txt = r.text
url = ''
lisurl=[]
lis = txt.split('\n')
for t in lis:
    if 'img' in t:
        print(1,t,'\n',t.split('src=')[-1].split('"')[1])
        url = t.split('src=')[-1].split('"')[1]
        print(2,url)
        if 'http' in url:
            lisurl.append(url)
print(len(lisurl))
for l in lisurl:
    try:
        r = requests.get(l)
        r.raise_for_status()
        abc = r.content
        filename = l.split('/')[-1]
        f=open(filename,'wb')
        f.write(abc)
        f.close()
        print('保存图片成功！')
    except:
        print('保存图片失败！')
