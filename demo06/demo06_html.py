#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(serl, tag, attrs):
        # print('<%s>' % tag)
        #if 'class' in attrs:
            print('> > > %s' % attrs)

    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        print('= = = =: %s' % attrs)

    def handle_data(self, data):
        # print(data)
        pass

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

if '__main__' == __name__:
    parser = MyHTMLParser()

    from contextlib import closing
    from urllib.request import urlopen
    with closing(urlopen('https://www.python.org/events/python-events/')) as page:
        for line in page:
            parser.feed(str(line, encoding="utf-8"))
    

    # feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

    # 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来
