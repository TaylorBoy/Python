# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取验证码并保存到本地
import re
import urllib.request as reqst
import urllib.parse
from http import cookiejar

class FAFU:

    def __init__(self):
        self.opener = None
        self.checkUrl = 'http://jwgl.fafu.edu.cn/(v32fex45kxlk4z45v02lwy55)/CheckCode.aspx'
        self.postUrl = 'http://jwgl.fafu.edu.cn/(v32fex45kxlk4z45v02lwy55)/default2.aspx'

    # 获取验证码并保存到图片文件
    def getCheckCode(self):
        # Cookie
        cookie = cookiejar.CookieJar()
        handler = reqst.HTTPCookieProcessor(cookie)
        self.opener = reqst.build_opener(handler)
        # 获取验证码
        checkCode = self.opener.open(self.checkUrl).read()
        with open('code.jpg', 'wb') as checkCodeImg:
            checkCodeImg.write(checkCode)

    def login(self):
        username = str(input('username: '))  # Default string.
        password = str(input('password: '))
        checkcode = str(input('checkcode: '))
        postData =  urllib.parse.urlencode({
            '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz5xQU1YXNHacgTbKvSXBd9SngM+XA==',
            '__VIEWSTATEGENERATOR': '92719903',
            'txtUserName': username,
            'TextBox2': password,
            'txtSecretCode': checkcode
        }).encode(encoding='utf-8')

        # 登录
        self.opener.open(self.postUrl, postData)

        # 利用cookie请求访问另一个网页
        testUrl = 'http://jwgl.fafu.edu.cn/(v32fex45kxlk4z45v02lwy55)/xs_main.aspx?xh=' + username
        pageData = self.opener.open(testUrl).read()
        data = str(pageData, encoding='gb2312')
        print(data)


if __name__ == '__main__':
    fafu = FAFU()
    fafu.getCheckCode()
    fafu.login()