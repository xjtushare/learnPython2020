# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))
    #print('{}, {}'.format(index, obj))


# 一、字符串下标
# 1、下标访问字符
word = "hello"

func(0, word[0])
#func(0, word[5])#错误示范

# 负数下标：从后往前数
func(1, word[-1])

# 下标截取字符串,默认步长为1，包头不包尾
func(2, word[1:3])
str1 = "01234"
func(3, str1[2:5:2])
# 倒序字符串
func(4, str1[::-1])
# 获取字符串后三位字符
func(5, str1[-3:])
#复制字符串
func(6, str1[:])

# 二、字符串方法

# 长度
name='abcda'
func(7, len(name))

# 查找字串,有，返回index，否则-1
func(8, name.find("e")) #返回第一次出现的位置
func(9, name.find("a"))

# 字串出现次数
func(10, name.count("a"))

# 是否包含 in, not in
func(11, 'bc' in name)
func(12, 'bc' not in name)

# 字符串替换
func(19, name.replace("a", "k"))

# 字符串分割
num = "1,2,3,4,5,6"
num1 = "123456"
func(20, num.split(","))
func(21, num1.split("23"))

# 转义字符
"""
\"  "
\\  \
\t  tab
\n  newline

字符串中转义字符失效,加r
r"D:\data"
"""
str2 =r"\n 表示换行"
#str2 ="\n 表示换行" #示范转义字符生效
func(22, str2)

# 换行字符串 """,或'''
html = """
<html>
    <head>
    </head>
    <body>
    </body> 
</html>
"""
func(23, html)


# 格式化字符串

age = 20
name = "book"
# 拼接方式

# 方式1、F-String(Python3.6以上)
result1 = f"年龄是:{age}岁"
func(24, result1)

# 方式2、format()，{}作为占位符，format传入参数
result2 = "你好{},年龄是:{}岁".format(name, age)
#result2 = "你好{0},年龄是:{0}岁".format(name, age)
#result2 = "你好{0},年龄是:{1}岁".format(name, age)
func(25, result2)

# 方式3、% 根据变量类型来写
result3 = "你好%s,年龄是:%d岁" % (name, age)
func(26, result3)

print(type(result3))


