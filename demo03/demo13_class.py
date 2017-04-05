#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):   # 继承自object

    def __init__(self, name, score):
        self.name  = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

stu = Student('Taylor Boy', 77)
stu.print_score()
    
# 权限: private, public, protected
class Person(object):
    __slots__ = ('__name', '_score')   # 限制实例的属性, 只允许添加__name和_score属性
    def __init__(self, name, score):
        self.__name = name  # private: 以双下划线开头, 不能被外部访问(其实可以访问_Student__name)
        self._score = score # protected, 实际没作用
                            # __test__: 以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的
prs = Person('Mkit', 88)                         

# 获取对象信息: type()
print(type(123))
print(type(stu))
print(type(prs))

# 如果要判断一个对象是否是函数: types.FunctionType
import types
print(str(type(abs) == types.BuiltinFunctionType))
print(str(type(lambda x: x * x) == types.LambdaType))
print(str(type((x for x in range(10))) == types.GeneratorType))

# 判断一个对象是什么类型: isinstance()
print(str(isinstance(stu, Student)))
print(str(isinstance(stu, object)))  # 继承

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(stu))
# 有x属性吗:    hasattr(obj, 'x')    // has attribute
# 设置一个y属性: setattr(obj, 'y', 88)
# 获取属性y:    getattr(obj, 'y')
# 获取属性'z', 如果不存在, 返回默认值404: getattr(obj, 'z', 404) 

