#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

    @property
    def width(self):          # width_getter()
        return self._width

    @width.setter
    def width(self, value):   # width_setter(value)
        self._width = value

    @property
    def height(self):
        return self._heigth

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return 786432

# test:
s = Screen()
s.width = 1024
s.height = 768

assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
print(s.resolution)

