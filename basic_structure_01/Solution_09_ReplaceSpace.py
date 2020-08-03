# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy.

"""

class Solution_09_ReplaceSpace:
    def replaceSpace(self,s):
        '''
        初始化一个空列表
        遍历字符串的每一个字符
        如果是某一个字符，则直接把该字符添加到列表
        如果遍历到的一个空字符，则把%20添加到列表中
        最后通过''.join(列表名)把列表转为字符串即可
        :param s:
        :return:
        '''
        aa = []
        #说明：下标从0开始，字符串最后一个字符的index是len(s)-1
        for i in range(0,len(s)):
            if s[i] == ' ':
                aa.append("%20")
            else:
                aa.append(s[i])
        return ''.join(aa)


if __name__ == '__main__':
    result = Solution_09_ReplaceSpace()
    s1 = "We Are Happy."
    print(result.replaceSpace(s1))