# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

# 添加 headers 验证
headers = {'User-Agent': user_agent}

req = urllib.request.Request(url, headers=headers)

### 1. 异常处理 URLError
# * reason属性
# 网络无连接，即本机无法上网
# 连接不到特定的服务器
# 服务器不存在
try:
    reqst = urllib.request.Request('http://www.taylorxxxxx.com')
    urllib.request.urlopen(reqst)
    print('OK')
except urllib.request.URLError as e:
    print(e.reason)

# 2.HTTPError
# * code属性
# HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”
reqst = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(reqst)
except urllib.request.HTTPError as e:
    print('Code: ', e.code)
except urllib.request.URLError as e:
    print('Reason: ', e.reason)
else:
    print('Done !')

if __name__ == '_main__':

    pass

