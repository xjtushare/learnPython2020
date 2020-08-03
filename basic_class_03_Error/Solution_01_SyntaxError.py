# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
语法错误
SyntaxError

1、忘记在 if，for，def，elif，else，class 等声明末尾加:
或者
使用= 而不是 ==也会导致SyntaxError: invalid syntax
= 是赋值操作符，而 == 是等于比较操作
会导致SyntaxError ：invalid syntax如下
"""

# def func(num):
#     if num == 1
#         print("a")
#
# func()

# def func1(num):
#     if num = 1
#         print("a")
#
# func1()


"""
2、在字符串首尾忘记加引号
导致SyntaxError: EOL while scanning string literal
在字符串首尾忘记加引号
"""

# print('my name is '+ beijing')

"""
3、尝试使用 Python 关键字作为变量名
导致SyntaxError：invalid syntax
Python 关键不能用作变量名

    class = 'home'
          ^
SyntaxError: invalid syntax



Python3 的关键字有：
and, as, assert, break, class, continue,
def, del, elif, else, except, False, finally, 
for, from, global, if, import, in, is, lambda, 
None, nonlocal, not, or, pass, raise, return, 
True, try, while, with, yield

"""
#
# class = 'home'
# print(class)



"""
4、不存在 ++ 或者 -- 自增自减操作符
正确写法：
 a += 1
 a = a+1
 
 错误提示：
     m++
      ^
SyntaxError: invalid syntax
"""

'''
错误示范
'''
# m = 0
# m++
# print(m)

'''
正确示范
'''
# m=0
# m += 1
# print(m)

