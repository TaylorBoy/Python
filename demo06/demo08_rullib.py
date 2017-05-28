# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. urllib的request模块可以非常方便地抓取URL内
#    也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))

# 2. 模拟浏览器发送GET请求, 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
#    模拟iPhone 6
req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status: ', f.status, f.reason)
    for (k, v) in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', f.read().decode('utf-8'))
