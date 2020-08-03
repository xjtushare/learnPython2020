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

        # write code here
        #1 2 3 4 
        #3 4 5 6
        #5 6 7 8 
        
解法二：从右上角的元素开始查找       
'''


class Solution_06_TwoArrayFind :
    def Find(self, target, array) :
        # 找到右上角元素的索引或者下标
        i = 0
        j = len(array[0]) - 1
        # 行数
        row_count = len(array)
        col_count = len(array[0])
        # 保证查找过程中不越界
        '''
        因为从右上角开始找，i++；j--
        '''
        while i < row_count and j >= 0 :
            if array[i][j] == target :
                return True
            elif array[i][j] > target :
                j = j - 1
            else :
                i = i+1
        return False

if __name__ == '__main__' :
    array=[[1,2,4],[6,8,12],[9,10,54]]
    result = Solution_06_TwoArrayFind()
    print(result.Find(6, array))
