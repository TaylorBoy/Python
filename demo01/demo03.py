#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('我的Python中文编码测试 !')

# 格式化输出: %与c一致, %% == '%'
name = input('Please input your name: ')
print('Hello %s, I am Tyalor' % name)
print('%s like %s very much!' %('Taylor', name))
# %s永远会把任何数据转化为字符串
print('%s %s %s %s' %(3.14, 'Hello', 88, -96))
