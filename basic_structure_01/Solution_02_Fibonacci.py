# !/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
"""
要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）

斐波那契（Leonardoda Fibonacci）数列：0、1、1、2、3、5、8、13、21、34...
"""
"""
非递归实现
"""
class Solution_01_Fibonacci:
    def Fibonacci(self, n) :
        if n==0:
            return 0
        if n==1:
            return 1
        a=1
        b=0
        result = 0
        for i in range(0,n-1):
            result = a+b
            b = a
            a = result
        return result
if __name__ == '__main__':
    t1 = datetime.datetime.now().microsecond
    result = Solution_01_Fibonacci()
    print(result.Fibonacci(100))
    t2 = datetime.datetime.now().microsecond
    print("Total time:",(t2 - t1))

