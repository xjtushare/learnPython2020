# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution_03_JumpFloor:
    def jumpFloor(self, number) :
        # write code here
        # n=1 1
        # n=2 2
        # n=3 1+2=3 111 12 21
        # n=4 1111 22 112 121 211  3+2=5
        # => f(n) = f(n-1)+f(n-2) n>=3
        if number <= 0 :
            return 0
        if number == 1 :
            return 1
        if number == 2 :
            return 2
        a = 1
        b = 2
        result = 0
        for i in range(3, number+1) :
            result = a + b
            a = b
            b = result
        return result

if __name__ == '__main__':
    target = Solution_03_JumpFloor()
    print(target.jumpFloor(4))