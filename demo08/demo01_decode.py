#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import importlib
importlib.reload(sys)

if __name__ == '__main__':

    with open('ansi.cpp', 'r') as file:
        with open('test.cpp', 'w') as fwrite:
            while True:
                line = file.readline()
                if not line:
                    break
                # print(type(line.encode("utf-8"))) # bypes
                s = line.encode('utf-8')
                fwrite.write(s.decode('utf-8'))

