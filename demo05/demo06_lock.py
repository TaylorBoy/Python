#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()    # 获取锁
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()    # 释放锁

def multicore():
    l  = mp.Lock()   # 定义一个进程锁
    v  = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()

# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务



