# !/usr/bin/env python
# -*- coding:utf-8 -*-

def func(index, obj):
    print('{%d}, %s' % (index, obj))


"""
    1、先打开文件，才能访问它
    read()到达文件
    末尾时返回一个空字符串，显示出来就是一个空行
    要删除多出来的空行，可以print语句中使用rstrip():
"""
# 1、读取整个文件
file_path = '/Users/sudo/Documents/test_data/file.txt'
with open(file_path) as f1:
    contents = f1.read()
    func(1, contents)
    func(1, contents.rstrip())
    func(2,"abc")

# 2、逐行读取
with open(file_path) as f1:
    for line in f1:
        func(3, line.rstrip())
        func(4, "ef")

"""
    注意：python读取文本文件时，将其中的所有文本都解读为字符串
    所以，如果读取为数字，需要使用int()转换为整数，float（）同理
"""
