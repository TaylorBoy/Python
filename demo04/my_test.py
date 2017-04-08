#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单元测试
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw);

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    d = Dict(a=1, b=2)
    print(d['a'])
    print(d.b)

