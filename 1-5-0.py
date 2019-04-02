import requests
url = 'http://m.ip138.com/ip.asp?ip='
'''您查询的IP：202.204.80.112</h1><p class="result">
本站主数据：北京市海淀区 北京理工大学 教育网</p><p class="result">
参考数据一：北京市 北京理工大学</p>'''
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    txt = r.text
    mark1 = txt.find('您查询的IP')
    mark3 = txt.find('</div>',mark1)
    if mark1 != -1 and mark3 != -1:
        txtReal = txt[mark1: mark3]
    else:
        print('查询数据失败！')
    txtProcess = ''
    flag = True
    for word in txtReal:
        if word == '<':
            flag = False
        if flag:
            txtProcess += word
            continue
        if word == '>':
            flag = True
    txtProcess = txtProcess.replace('\n','')
    print('查询结果为：\n{}'.format(txtProcess))
except:
    print('爬取失败！')
