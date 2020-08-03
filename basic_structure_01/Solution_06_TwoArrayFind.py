# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""
'''
O(m*n)

        # write code here
        #1 2 3 4 
        #3 4 5 6
        #5 6 7 8 
'''
class Solution_06_TwoArrayFind:
    def Find(self,target,array):
        #有多少个行
        for i in range(len(array)):
            #有多少列
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True
        return False


if __name__ == '__main__':
    arr1 = [[6],[1],[2],[10]]
    result = Solution_06_TwoArrayFind()
    print(result.Find(-2,arr1))