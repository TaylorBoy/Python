# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入
# 模拟微博登录
from urllib import request, parse

if __name__ == '__main__':
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('usrname', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status: ', f.status, f.reason)
        for (k, v) in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data: ', f.read().decode('utf-8'))

if __name__ == 'main__':
    print('Run...')


    def fetch_xml(url):
        with request.urlopen(url) as f:
            print('Status: ', f.status, f.reason)
            for (k, v) in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data: ', f.read().decode('utf-8'))

    # 测试
    print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))