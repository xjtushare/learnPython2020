# !/usr/bin/env python
# -*- coding:utf-8 -*-
def func(number):
    #number+1表示从3开始一直加到n
    for i in range(3, number+1) :
        print(i)

if __name__ == '__main__':
    func(6)