#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
# 创建目录

# 1. 获取当前绝对路径
pth = os.path.abspath('.')
print(pth)

# 2. 合并路径, 用join可以正确处理不同操作系统的路径分隔符
pth_new = os.path.join(pth, 'test_dir')
print(pth_new)

# 3. 创建目录
# os.mkdir(pth_new)

# t. 删除目录
# os.rmdir(pth_new)

# 拆分路径(只是对字符串拆分, 路径不一定存在)
t = os.path.split(pth_new)
print(pth_new)

# 获取文件扩展名
t2 = os.path.splitext(pth_new)
print(t2)

# 重命名
#os.rename(pth_new+'\\test.txt', pth_new+'\mytest.txt')


# 列出当前目录下的所有目录:
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)

# 列出所有的文件:
l2 = [x for x in os.listdir('.') if os.path.isfile(x)]
print(l2)

# 列出所有的.py文件:
l3 = [x for x in os.listdir('.')
      if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l3)

