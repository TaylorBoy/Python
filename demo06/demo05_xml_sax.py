#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# XML -- SAX
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        # print('sax: start_element: %s, attrs=%s' % (name, attrs))
        # 获取当天和第二天的天气
        # if attrs.has_key('date'): # python2.7
        if 'date' in attrs.keys():  
            print(str(attrs['date']), str(attrs['low']), str(attrs['high']), )
            print('*  *  **  *  *')
        

    def end_element(self, name):
        print('sax: end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
</ol>
'''


if __name__ == '__main__':
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
