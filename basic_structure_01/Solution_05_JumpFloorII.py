# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution_05_JumpFloorII:
    def jumpFloorII(self, number):
       if number == 1:
           return 1
       result = 1
       a = 1
       for i in range(2,number+1):
           result = 2*a
           a = result #a是上一次的 2*a结果
       return result

if __name__ == '__main__':
    result = Solution_05_JumpFloorII()
    print(result.jumpFloorII(4))