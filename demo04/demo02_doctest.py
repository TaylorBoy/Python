#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文档测试: doctest
def fact(n):
    '''
    Simple recursive function.
    
    >>> fact(3)  # 测试操作
    6            # 期望输出结果, 若不匹配则报错
    >>> fact(5)
    120
    >>> f = fact(5)
    >>> f
    12
    
    '''

    # 函数代码:
    if n < 1:
        raise ValueError( )
    if 1 == n:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

