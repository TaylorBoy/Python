#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数: 变量可以指向函数，函数的参数能接收变量，
#          那么一个函数就可以接收另一个函数作为参数

def my_add(x, y, func):
    return func(x) + func(y)

# map: 分开的, list map(f(x), [list])
def f(x):
    return x * x
ret = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(ret))

# reduce: 合并的, reduce(f(x, y), [list])
from functools import reduce

def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(f, map(char2num, s))

print(str2int('65535') + 1)


# Run1:
L1 = ['adam', 'LISA', 'barT']

def normalize(name):
    return name.capitalize()

L2 = list(map(normalize, L1))
print(L2)

# Run2: 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums  = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0  # 记录小数点
    
    def to_float(f, n):
        nonlocal point
        if -1 == n:         # 记录是否遇到小数点(小数点只有一个)
            point = 1
            return f
        if 0 == point:      # 有无小数点的计算
            return f * 10 + n       
        else:
            point = point * 10      # 计算小数点位置
            return f + (n / point)  # 计算小数值 (n / point)
        
    return reduce(to_float, nums, 0.0)   # reduce(func(x, y), map, init_value)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))    
    


