#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 进程池 Pool 和map()
import multiprocessing as multip

def func(x):
    return x * x

def multicore():
    pool = multip.Pool()
    res = pool.map(func, range(10))
    print(res)

# 用 apply_async() 输出多个结果
def multicore2():
    pool = multip.Pool()
    # apply_async()中只能传递一个值，它只会放入一个核进行运算
    res = [pool.apply_async(func, (i,)) for i in range(12)]
    print([r.get() for r in res])

if __name__  == '__main__':
    multicore()
    multicore2()
