#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 断言 assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero !'
    return 10 / n

def main():
    print(foo('01'))

# 启动Python解释器时可以用-O参数来关闭assert(相当于pass)
main()


# logging
import logging

# 配置消息级别: debug，info，warning，error
logging.basicConfig(level=logging.ERROR)

s = '01'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
