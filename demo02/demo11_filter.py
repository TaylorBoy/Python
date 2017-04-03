#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter筛选
# Iterator filter(f(x), [list])

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
#   然后根据返回值是True还是False决定保留还是丢弃该元素

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))

# 用filter求素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()   # 初始序列 3 5 7 9 11 13 15 ...
    while True:
        n = next(it)   # 返回筛选序列的第一个数, 3 
        yield n
        it = filter(_not_divisible(n), it)  # f(x) return x % n > 0
                                            #                 3

for x in primes():
    if x < 100:
        print(x)
    else:
        break

# 回文 -- 回数
def is_palindrome(n):
    ch = str(n)
    length = len(ch)
    count = int(length / 2)
    i = 1
    while True:
        x1 = length - i
        x2 = i - 1
        i += 1  
        if x1 >= count:
            if x1 != x2:
                if ch[x1] == ch[x2]:
                    continue
                else:
                    return False
        else:
            break
    return True
        
    

output = filter(is_palindrome, range(1, 1000))
print(list(output))

    
