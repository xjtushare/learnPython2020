# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time

"""
当一个函数中，不同逻辑混杂在一起的时候，程序的可读性会大打折扣。这个时候，可以考虑用一种叫做“装饰器”的东西来重新整理代码。
从一个简单的例子出发，简单介绍了python中装饰器的用法
"""


# 装饰器

#判断质数 效率O(n)
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


#2、想输出1到10000之间的所有质数
"""
说明，创建好一个装饰器之后，就把这段代码修改
"""
# def prime_nums():
#     t1 = time.time()
#     for i in range(2,10000):
#         if is_prime(i):
#             print(i)
#     t2 = time.time()
#     print(t2-t1)

#运行，看下效率
#prime_nums()

#3、现在我想测试下这段代码的时间,引入time包，代码前后加入t1,t2
#看出运行时间是0.49390578269958496，即0.4秒左右

'''
def prime_nums():这段代码
即包含了计算时间，也包含了判断质数，可读性非常低
为了解决这个问题，把逻辑和计时分开，就需要用到一个叫做装饰器的东西
'''

"""
使用装饰器，必须先起个名字，实质也是函数
比如求总的时间

装饰器的参数是另外一个函数，
func意思是等同于运行函数 prime_nums

装饰器里面再写一个函数wrapper(),表示要运行func函数的时候，要运行哪些内容
"""

def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)
    return wrapper

"""
接下来是写好的这个装饰器怎么应用到 def prime_nums():这个函数上面
首先把时间都删除，只保留2到10000之间求所有质数的代码

1、在函数def prime_nums():上面加入@display_time
这样，当运行def prime_nums():函数的时候，其实运行的是装饰器
就是说：运行prime_nums()时候，直接跳到def display_time里面运行wrapper里面内容
先记时，然后运行func，才是prime_nums这个函数
    
"""
@display_time
def prime_nums():
    for i in range(2,10000):
        if is_prime(i):
            print(i)

prime_nums()

'''
如果是统计2到10000有多少个质数

'''
@display_time
def count_prime_nums():
    count =0
    for i in range(2,10000):
        if is_prime(i):
            count = count +1
    return count
count = count_prime_nums()
print(count)

"""
发现输出的是None，为什么呢？是因为返回值count并没有传入到func()这个函数里面进来

"""