#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ThreadLocal
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student， 还可以绑定其他变量，
# 如local_school.teacher等等。ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
# 用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程的student
    std = local_school.student
    print('Hello, %s(in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Taylor',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Mike'  ,), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

