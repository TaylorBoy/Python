#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# _thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time, threading

def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s is running.' % (threading.current_thread().name))

if __name__ == '__main__':
    print('Thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)
