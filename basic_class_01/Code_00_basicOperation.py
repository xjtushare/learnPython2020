# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 基础操作
"""
Python基础知识
知识点列表:
    数字和运算符
    变量、字符串
"""

# 1、运算符
def demoOperation():
    # 取余运算，对2取余，结果0或1，可判断奇偶
    func(0, 4 % 2)  # 求余
    func(1, 5 + 2)
    func(2, 5 - 2)
    func(3, 5 * 2)

    # 除法运算结果总是浮点数
    func(4, 5 / 2)
    func(5, 2 / 2)
    # 整数除法，自动舍去小数，保留整数
    func(6, 5 // 2)
    func(7, 5 // 2.0)

    # 整除应用：获取某一位上的数字
    print("54321的万位数是：" + str(54321 // 10000))
    # print((54321 // 10000))
    # print(54321%10) #个位
    # print((54321 // 1000)) #万位和千位
    func(8, 5 << 2)
    func(9, 5 >> 2)  # 右移两位，低位移除，高位补0
    func(10, 5 & 2)  # 相同为1，不同为0
    func(11, 5 | 2)  # 只要有一个为1，其值为1
    func(12, 5 ^ 2)  # 相同为0不同为1，即求差异
    func(13, 5 == 2)
    func(14, 5 <= 2)
    func(15, 5 < 2)
    func(16, 5 != 2)
    # 指数运算
    func(17, 5 ** 2)  # 两个乘号表示乘方运算


# 2、注释，单引号，双引号，#号 均可

# 3、变量
    """
    就是存储数据的容器
    变量名只能为字母、数字，下划线，不能以数字开头
    可采用下划线，一般习惯上小写
    """

# 4、赋值 "="
    # 变量使用前必须赋值，并且"=左边必须为变量"

    greet = "hello Python!"
    func(18, greet)

    a = 2
    a += 6  #a= a+6
    func(19, a)

    # 多个变量同时赋值（不建议）
    m, n, k = 1, 2, 3
    func(20, m + n + k)


# 5、字符串（可以是单引号，双引号）

    # 字符串拼接 字符串只能拼接字符串类型
    part_one = "后浪们"
    part_two = "加油"
    part = part_one + part_two
    func(21, part)

    #类型转换 字符串中使用整数时，需要将非字符串值转换为字符串
    func(22, ("你好" + str(1)))
    #func(23, ("你好" + 1)) #错误示范

    """
    说明：
    字符串使用 "+"和"*"运算符
    "+" 拼接
    "*" 重复字符串一定次数，产生新字符串
    """
    func(23, "hello" * 3)


demoOperation()
