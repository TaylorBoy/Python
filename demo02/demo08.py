#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式: List Comprehensions

# 生成[1x1, 2x2, 3x3, ...]
L1 = [x * x for x in range(1, 11)]

print(L1)

# if筛选
L2 = [x * x for x in range(1, 11) if 0 == x % 2]

print(L2)

# 两层循环
L3 = [ m + n for m in 'ABC' for n in 'XYZ']

print(L3)

# @ 列出当前目录下所有文件和目录名:
import os   # 导入os模块
L4 = [d for d in os.listdir('.')]

print(L4)

# 两个变量
d = {'T': 'A', 'a': 'B', 'y': 'B', 'l': 'C'}
L5 = [ key + ':' + val for key, val in d.items()]

print(L5)

# 将所有大写转为小写
L = ['Hello', 'World', 'IBM', 'Apple']
L6 = [s.lower() for s in L]

print(L6)

# 数据类型不一样
L_2 = ['Hello', 'World', 18, 'Apple', None]

L7 = [ s.lower() for s in L_2 if isinstance(s, str)]

print(L7)

