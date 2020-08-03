# !/usr/bin/env python
# -*- coding:utf-8 -*-

# lambda

def f(x):
    return x * x


print(f(5))
"""
所有有一行或一句话可以表达的都可以用lambda表达式写出来
lambda表达式：即只有一行代码的表达式
f = lambda x: x * x
           输入 :分开  输出
"""

f1 = lambda x: x * x

print(f1(5))

f2 = lambda x,y:x+y
print(f2(4,5))

"""
lambda应用：
    排序时，选择通过不同项进行排序  
"""
