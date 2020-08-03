# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
UnboundLocalError
在定义局部变量前在函数中使用局部变量
（此时有与局部变量同名的全局变量存在）


导致
UnboundLocalError: local variable 'a' referenced before assignment

在函数中使用局部变量而同时又存在同名全局变量时是很复杂的，使用规则是：
如果在函数中定义了任何东西，如果它只是在函数中使用那它就是局部的，反之就是全局变量。
这意味着你不能在定义它之前把它当全局变量在函数中使用。
"""


a = 2
def func():
    print(a)
    a = 100
func()