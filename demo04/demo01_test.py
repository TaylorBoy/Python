#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单元测试: 引入Python自带的unittest模块
import unittest

from my_test import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1, 'Value \'a\' error')  # 断言函数返回的结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertTrue(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # setUP & tearDown
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
