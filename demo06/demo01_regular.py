#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':

    email = input('Please input your e-mainl: ')

    # 切分字符串: split
    l = re.split(r'\s*', email)
    print(l)
    email_str = ''
    for s in l:
        email_str += s
    print(email_str)

    if re.match(r'^\d{4,11}@[0-9a-zA-Z\_]+\.\w{1,10}$', email_str):
        print('Ok')
    else:
        print('Error')

    # 分组 group: ()
    g = re.match(r'^(\d{3,11})@([0-9a-zA-Z\_]+\.\w{1,10})$', email_str)
    print('group(0): ', g.group(0))
    print('group(1): ', g.group(1))
    print('group(2): ', g.group(2))

    # 贪婪匹配: 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
    # >> > re.match(r'^(\d+)(0*)$', '3146004077000').groups()
    # ('3146004077000', '')
    # 加个?就可以让\d+采用非贪婪匹配
    # >> > re.match(r'^(\d+?)(0*)$', '3146004077000').groups()
    # ('3146004077', '000')

    # 预编译: 如果一个正则表达式要重复使用几千次
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    t = re_telephone.match('010-57856').groups()
    print(list(t))



