# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time

"""
发现输出的是None，为什么呢？是因为返回值count并没有传入到func()这个函数里面进来
先把装饰器里面的func()返回值，先记录起来，放到result里面进去，
然后在函数wrapper()里面，把result再次返回出来，发现运行结果1229
"""
def display_time(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print("Total time:{:.4}s".format(t2 - t1))
        return result
    return wrapper


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

#如果是统计2到10000有多少个质数

@display_time
def count_prime_nums():
    count =0
    for i in range(2,10000):
        if is_prime(i):
            count = count +1
    return count
count = count_prime_nums()
print(count)




