#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器decorator

# 1
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# @语法，把decorator置于函数的定义处
@log        # 相对于 now = log(now)
def now():
    print('2017-04-03')

# Run
now()
print('now() now is: %s' % now.__name__)  # now()的名字变了

# 2

# functools 复制原函数属性
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)   # 复制属性
        def wrapper(*args, **kw):
            print('%s -- call %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 三层嵌套的decorator
@log('test')  # now = log('execute')(now)
def now2():
    print('2017-04-03 15:32')

now2()
print('now2() now is %s' % now2.__name__)


print('>>>>>>>>>>>>>>>>>>>>>>>>')
# Run2: 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def mylog(func):
    def wrapper(*args, **kw):
        print('Call function...')
        return func(*args, **kw), print('End call...')
    return wrapper

def mylog2(*args, **kw):
    def decorator(func):
        def wrapper(*args, **kw):
            print('Call function...')
            return func(*args, **kw), print('End call...')
        return wrapper
    return decorator

@mylog2('test')
def test():
    print('MY decorator test...')

test()

#################################################
# 偏函数partial function:
print(int('1234', base=8))

def int2(x, base=8):
    return int(x, base)

print(int2('1234'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
import functools
int8 = functools.partial(int, base=8)
print(int8('1234'))
