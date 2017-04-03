#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:   # 默认迭代key
    print(key)

for val in d.values():
    print(val)

for key, val in d.items():
    print(key, val)

# String is the same too.
for ch in "Taylor":
    print(ch)


# 判断是否可迭代: Iterable
from collections import Iterable
print('\'abs\' is ', str(isinstance('abs', Iterable)))
print('\'123\' is ', str(isinstance(123  , Iterable)))

# 对list实现下标操作: enumerate --枚举
for index, value in enumerate(['A','B','C']):
    print(index, '-->', value)

# Two variable.
for x, y in [(1,2),(3,4),(5,6)]:
    print('(', x, y,')')
