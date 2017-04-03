#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器: generator

# 第一种方法很简单，只要把一个列表生成式的[]改成()
L1 = (x * x for x in range(10))

# 一般用for循环迭代
for n in L1:
    print(n)

# 用函数实现生成器: Fibonacci
def fibo(end):
    n, a, b = 0, 0, 1
    while n < end:
        print(b)
        a, b = b, a + b
        # t = (b, a + b) # t是一个tuple
        # a = t[0]
        # b = t[1]
        n += 1
    return 'done'

# Generator 每次调用 next() 时遇到 yield 返回, 知道没有下个 yield
def gfibo(end):
    n, a, b = 0, 0, 1
    while n < end:
        yield (b)
        a, b = b, a + b
        n += 1
    return 'done'

# 杨辉三角
def triangles():
    L1 = [0] * 22
    L2 = [0] * 22
    L1[0] = 1

    n = 0
    while n <= 10:
        t  = L1
        L1 = L2
        L2 = t
        print(L2)
        t = 1
        L1[0] = 1
        while t <= n + 1:
            L1[ t ] = L2[t] + L2[ t-1 ]
            t += 1        
        n += 1
    return 'DONE'

# 别人家的三角
def triangle():
    L = [1]
    while True:
        yield (L)
        L = [ L[x] + L[x+1] for x in range(len(L) - 1)] #计算下一行中间的值（除去两边的1）
        L.insert(0,1)                                   #在开头插入1
        L.append(1)                                     #在结尾添加1
        if len(L)>10:                                   #仅输出10行
            break

            


        
        
