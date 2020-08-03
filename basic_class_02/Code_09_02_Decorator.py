# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time

"""
如果函数带参数，装饰器怎么修改
比如现在我想输出任意范围的质数，而不是10000
"""

def display_time(func):
    #*args表示我不知道有多少个参数
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
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
def count_prime_nums(MaxNum):
    count =0
    for i in range(2,MaxNum):
        if is_prime(i):
            count = count +1
    return count
count = count_prime_nums(10000)
print(count)




