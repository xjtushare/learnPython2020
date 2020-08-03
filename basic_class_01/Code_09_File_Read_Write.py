# !/usr/bin/env python
# -*- coding:utf-8 -*-

file = '/Users/sudo/caiji/python_code/test.txt'
result = '123456'
with open(file,'r') as f2:
    print("写入文件之前，test.txt文件内容是："+f2.read())

with open(file,'w') as f1:
    f1.write(result)

with open(file,'r') as f2:
    print("写入文件后，test.txt文件内容是："+f2.read())
