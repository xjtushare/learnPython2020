# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""

class Solution_10_TwoStackImplementQueue:
    '''
    实现思路：
    把一个栈压入的元素倒入到另一个栈输出，即先进先出，队列的效果
    '''
    def __init__(self):
        '''
        定义两个栈，接收栈和输出栈
        '''
        self.acceptStack = []
        self.outputStack = []
    '''
        另外一种写法：
        def __init_(self,acceptStack=[],outputStack=[]):
            self.acceptStack = acceptStack
            self.outputStack = outputStack
    '''
    def push(self,node):
        '''
        压栈：
            把node压入到接收栈里去
        :param node:
        :return:
        '''
        self.acceptStack.append(node)

    def pop(self):
        '''
        弹栈
            输出栈如果为空，接收栈不为空，则
        接收栈弹出一个，输出栈压入一个
            输出栈如果不为空，则弹出栈顶元素
            否则，即输出栈为空，接收栈为空情况，返回None
        :return:
        '''
        if self.outputStack == []:
            while self.acceptStack != []:
                self.outputStack.append(self.acceptStack.pop())
        elif self.outputStack != []:
            return self.outputStack.pop()
        else:
            return None

if __name__ == '__main__':
    testQueue = Solution_10_TwoStackImplementQueue()
    testQueue.push(1)
    testQueue.push(2)
    testQueue.push(3)
    testQueue.push(4)
    

