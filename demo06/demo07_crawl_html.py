# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import os

class MyHTMLPaser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.li = False
        self.h3 = False
        self.a = False
        self.p = False
        self.time = False
        self.span1 = False
        self.span2 = False
        self.event_dict = {}
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if 'li' == tag:
            self.li = True
        elif 'h3' == tag:
            for k, v in attrs:
                if k == 'class' and v == 'event-title':
                    self.h3 = True
        elif 'a' == tag:
            self.a = True
        elif 'p' == tag:
            self.p = True
        elif 'time' == tag:
            self.time = True
        elif 'span' == tag:
            for k, v in attrs:
                if k == 'class' and v == 'say-no-more':
                    self.span1 = True
                elif k == 'class' and v == 'event-location':
                    self.span2 = True

    def handle_data(self, data):
        if self.li:
            if self.h3 == True and self.a == True:
                self.count += 1   # 用self.count作为self.IDdict的key，表示会议的次数
                self.event_dict[self.count] = {}
                self.event_dict[self.count]['name'] = data
            elif self.p:
                if self.time:
                    if not self.span1:
                        self.event_dict[self.count]['time'] = data
                    else:
                        self.event_dict[self.count]['time'] += (',' + data)
                else:
                    if self.span2:
                        self.event_dict[self.count]['site'] = data

    def handle_endtag(self, tag):
        if 'a' == tag:
            self.a = False
        elif 'h3' == tag:
            self.h3 = False
        elif 'span' == tag:
            self.span1 = False
            self.span2 = False
        elif 'time' == tag:
            self.time = False
        elif 'p' == tag:
            self.p = False
        elif 'li' == tag:
            self.li = False

parser = MyHTMLPaser()

def parser_event(html_data):
    global parser
    parser = MyHTMLPaser()
    parser.feed(html_data)
    return parser.event_dict

if '__main__' == __name__:

    # with open('.\\test.html', 'r', encoding="utf-8") as fhtml:
    #     event = parser_event(fhtml.read())
    from urllib.request import urlopen
    html = urlopen('https://www.python.org/events/python-events/').read()
    event = parser_event(str(html))

    for i in range(1, parser.count+1):
        print(event[i]['name'], '\n', event[i]['time'], '\t', event[i]['site'])
