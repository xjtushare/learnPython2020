# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""

TypeError

例1：在 for 循环语句中忘记调用 len()
导致TypeError: 'list' object cannot be interpreted as an integer
通常你想要通过索引来迭代一个 list 或者 string 的元素，这需要调用 range() 函数。
要记得返回 len 值而不是返回这个列表
"""

aa = ['cmbc','libai','chinese']

'''
错误示范
'''
# for i in range(aa):
#     print(aa[i])


'''
正确写法
'''
for i in range(len(aa)):
    print(aa[i])


"""
例2：
尝试修改 string 的值
导致TypeError: 'str' object does not support item assignment
string 是一种不可变的数据类型
"""

'''
错误示范
TypeError: 'str' object does not support item assignment
错误内容：不支持字符串的修改

'''
# str1 = 'come here'
# str1[1]='o'
# print(str1)

'''
正确做法
'''
str1 = 'come here'
str1 = str1 + 'r'+str1[:2]
print(str1)


"""
例3：尝试连接非字符串值与字符串
导致 TypeError: Can't convert 'int' object to str implicitly
这里报错的意思就是这个语句里面含有对象为整型的数据，不能直接赋予字符串类型
"""

'''
错误示范
'''
# print('I have'+18+'ages')


'''
正确示范
'''
print('I have '+str(18)+' ages')
print('I have %s ages' %(18))


"""
例4、尝试使用 range()创建整数列表
导致TypeError: 'range' object does not support item assignment
有时你想要得到一个有序的整数列表，所以 range() 看上去是生成此列表的不错方式。
然而，你需要记住 range()返回的是 range object，而不是实际的 list 值。

"""

'''
错误示范
TypeError: 'range' object does not support item assignment

注意：在 Python 2 中 a = range(10)是能行的，
因为在 Python 2 中 range()返回的是list值，但是在 Python 3 中就会产生以上错误.
'''
# a  = range(5)
# a[2] = 0

'''
正确示范
'''
# a  = list(range(5))
# a[2] = 0


"""
例5、忘记为方法的第一个参数添加 self 参数
导致TypeError: myMethod() takes no arguments (1 given)

   a.func()
TypeError: func() takes 0 positional arguments but 1 was given

"""

# class Solution():
#     def func():
#         print('Hello!')
# a = Solution()
# a.func()