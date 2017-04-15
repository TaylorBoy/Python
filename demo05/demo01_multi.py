#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Linux上有fork, 而windows上用multiprocessing的Process
from multiprocessing import Process
import os

# Child.
def son_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % (os.getpid()))
    # 创建子进程
    son = Process(target=son_proc, args=('test',))
    print('Child process will start.')
    son.start()
    son.join()   # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
