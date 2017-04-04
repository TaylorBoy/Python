#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 内置的sorted()函数就可以对list进行排序
sorted([36, 5, -12, 9, -21])

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
sorted([36, 5, -12, 9, -21], key=abs)

# Run
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# Sorted by name.
def by_name(t):
    return t[0].lower()

# Sorted by score.
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
#print(L2)

L2 = sorted(L, key=by_score)
#print(L2)

# 利用operator的itemgetter获取元素更快
from operator import itemgetter

print(sorted(L, key=itemgetter(0)))

#lambda
print(sorted(L, key=lambda t: t[1]))

