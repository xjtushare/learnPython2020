# !/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
"""
要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）

斐波那契（Leonardoda Fibonacci）数列：0、1、1、2、3、5、8、13、21、34...
"""

"""
递归实现
"""

class Solution_01_Fibonacci:

    def Fibonacci(self, n) :

        if n==0:
            return 0
        if n==1:
            return 1
        if n>1:
            num = self.Fibonacci(n-1)+self.Fibonacci(n-2)
            return num

        return None
if __name__ == '__main__':
    t1 = datetime.datetime.now().microsecond
    result = Solution_01_Fibonacci()
    print(result.Fibonacci(100))
    t2 = datetime.datetime.now().microsecond
    print("Total time:",t2-t1)



"""
执行结果： 运行超时:您的程序未能在规定时间内运行结束，
请检查是否循环有错或算法复杂度过大。 用例通过率: 0.00% 运行时间: 2001ms 占用内存: 0KB
"""
