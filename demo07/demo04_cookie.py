# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
from http import cookiejar

# CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

if __name__ == 'main__':
    # 声明一个CookeiJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
    cookier = urllib.request.HTTPCookieProcessor(cookie)
    # 通过cookier来构建opener
    opener = urllib.request.build_opener(cookier)
    # open和urlopen同, 可传入request
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name : ' + item.name)
        print('Value: ' + item.value)

if __name__ == 'main__':
    # 保存cookie到文件
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    cookier = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookier)
    response = opener.open('http://www.baidu.com')
    # ignore_discard, 即使cookies将被丢弃也将它保存下来，
    # ignore_expires, 如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == 'main__':
    # 从文件中获取Cookie并访问
    filename = 'cookie.txt'
    # 创建MozillaCookieJar实例对象
    cookie = cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib.request.Request('http://www.baidu.com')
    # 创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print(response.read())

# 处理乱码
def tools(html):
    import re
    pattern = re.compile('<.*?>(.*?)<.*?>')
    content = re.findall(pattern, html)
    return content[0].encode('utf-8')


# 登陆测试, 密码需要修改
if __name__ == 'main__':
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    hander = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(hander)
    postdata = urllib.parse.urlencode({
        'logintoken': '1493472268691',
        'IPT_LOGINUSERNAME': '3146004077',
        'IPT_LOGINPASSWORD': 'XXXXXXXXXXX'
    }).encode(encoding='utf-8')

    # 登录, 保存cookie
    loginurl = 'http://jxpt.fafu.edu.cn/meol/loginCheck.do'
    result = opener.open(loginurl, postdata)
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 利用cookie请求访问另一个网页
    testUrl = 'http://jxpt.fafu.edu.cn/meol/jpk/course/layout/newpage1/index.jsp?courseId=11457'
    pageData = opener.open(testUrl).read()
    data = str(pageData, encoding='gb2312')
    print(data)
    # print(type(pageData))

# Cookie 测试 (cookie过期需要重新登录)
if __name__ == '__main__':
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    cookier = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookier)
    postdata = urllib.parse.urlencode({
        'logintoken': '1493472268691',
        'IPT_LOGINUSERNAME': '3146004077',
        'IPT_LOGINPASSWORD': 'xxxxxxxxxx'
    }).encode(encoding='utf-8')

    # 利用cookie请求访问另一个网页
    testUrl = 'http://jxpt.fafu.edu.cn/meol/jpk/course/layout/newpage1/index.jsp?courseId=11457'
    pageData = opener.open(testUrl).read()
    data = str(pageData, encoding='gb2312')
    print(data)