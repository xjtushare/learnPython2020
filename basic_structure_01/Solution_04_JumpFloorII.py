# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution_04_JumpFloorII:
    def jumpFloorII(self, number):
        # write code here
        #n=1 1 2的0次方
        #n=2 2 2的1次方
        #n=3 111 12 21 3   =>4 2的2次方
        #n=4 1111 22 112 211 121 13 31 4 =>8 2的3次方
        #n=n  2的n-1次方
        return pow(2,number-1)

if __name__ == '__main__':
    result = Solution_04_JumpFloorII()
    print(result.jumpFloorII(4))