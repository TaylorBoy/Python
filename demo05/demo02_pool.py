#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 线程池Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end   = time.time()
    print('Task %s run %.2f seconds.' % (name, end - start))

if __name__ == '__main__':
    print('Parent : %s ====>' % os.getpid())
    p = Pool(processes=3)   # 一般默认为cpu核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done.')
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
    p.close()
    p.join()
    print('All subprocesses done !')
