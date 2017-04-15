#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reading & Writing
try:
    f = open('./gbk.txt', 'r')
    print(f.read())  # read 可能出错
finally:
    if f:
        f.close()

# with 会为我们关闭文件.
with open('./gbk.txt', 'rb') as f:
    print(f.read())

# read(size) 读取固定字节
# readlines() 读取一行

# f = open('./test.txt', 'w+')
# f.write('Hello, I am Taylor')
# f.close()

# r只读，w可写，a追加
with open('./test.txt', 'a') as f:
    f.write('Hello I am Mike !\r\n')

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。
# 使用with语句操作文件IO是个好习惯
