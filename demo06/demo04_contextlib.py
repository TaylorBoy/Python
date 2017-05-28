#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### 1
# 并不是只有open()函数返回的fp对象才能使用with语句。
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('1. Begin...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error!')
        else:
            print('Done')

    def query(self):
        print('Query info about %s...' % self.name)

### 2
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法
# @contextmanager
from contextlib import contextmanager
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query inof: %s' % self.name)

# 这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去
@contextmanager
def create_query(name):
    print('2. Begin...')
    q = Query2(name)
    yield q
    print('Done')

### 2.2
# 希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

### 3
# 如果一个对象没有实现上下文，就不能把它用于with语句
# 可以用closing()来把该对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()


#################################################
if __name__ == '__main__':

    # 1
    with Query('Taylor') as q:
        q.query()

    # 2
    with create_query('Mike') as q2:
        q2.query()

    # 2.2
    # 代码的执行顺序是：
    # * 首先执行yield之前的语句
    # * 执行with语句内部的所有语句
    # * 最后执行yield之后的语句
    with tag('html'):
        print('Hello...')
        print('Python')

    # 3
    with closing(urlopen('https://www.python.org/events/python-events/')) as page:
        for line in page:
            print(line)
