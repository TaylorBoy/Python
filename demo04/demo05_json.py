#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化(json和pickle)
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age  = age
        self.score= score

# 1. 对象不是一个可序列化为JSON的对象, 需要转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'socre': std.score
    }

# 3. 把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
#    然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    s = Student('Taylor', 22, 77)
    print(json.dumps(s, default=student2dict))

    # 2. 或者用__dict__属性，它就是一个dict，用来存储实例变量(例外: 定义__slots__等)
    print(json.dumps(s, default=lambda obj: obj.__dict__))

    # 输出json到文件
    f = open("E:\\Code\\Python\\demo04\\test_dir\\mytest.txt", 'r')
    f.write(str(json.dumps(s, default=student2dict)))
    # print(json.loads(f.read(), object_hook=dict2student)) # 转为对象, Error
    f.close()

