# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 数据结构:列表
def demoList():
    # 列表  可变数据类型
    # 空列表
    a = []
    list1 = [1, 2.1, "a", False]
    func(1,type(list1))

    # 2、访问列表元素，下标,不能越界

    # python，索引从0开始
    func(2, list1[0])

    # 3、Python访问最后一个元素，通过将索引指为-1，同理：-2表示返回倒数第二个元素
    func(3, list1[-1])
    func(4, list1[-2])

    # 4、排序，必须是同一类型
    list2 = ['c', 'd', 'a', 'b']
    list2.sort()
    func(5, list2)

    # 5、反转列表,截取不影响原列表，reverse改变了原来的列表
    list3 = list2[::-1]
    func(6, list3)

    list2.reverse()
    func(7, list2)

    # 6、获取列表元素个数
    func(8, len(list2))

    # 7、获取最后一个元素的下标
    func(9, len(list2) - 1)


    # 9、python切片或截取（处理列表中的部分元素）
    # 需要指定起止索引，包头不包尾
    list4 = [1, 2.1, "H", False]
    func(10, list4[0:2])
    func(11, list4[:2])
    func(12, list4[1::2])

    # 复制列表
    func(13, list4[:])
    # 反向截取
    func(14, list4[::-1])
    # 截取不影响原来的列表
    func(15, list4)

    # 判断元素是否包含在列表中
    a = [1, 2, 3, 4]
    if 5 in a:

        func(16, "a包含这个元素")
    else:
        func(17, "a不包含这个元素")

    # 列表的拼接
    b1 = ['a', 'b', 'c', 'c']
    new_list = a + b1
    func(18, new_list)

    # 查找元素
    func(19, b1.index('b'))
    # 出现的次数
    func(20, b1.count('c'))
    # 交换列表中两个元素位置
    b1[0], b1[1] = b1[1], b1[0]
    func(21, b1)

    # 字符串和列表相互转换
    s = "周一、周二、周三、周四"

    # 字符串转列表
    a = s.split(",")
    func(22, a)

    # 列表转字符串
    # s2 = "".join(a)
    s2 = ",".join(a)
    func(23, s2)

    # 8、增删改查 元素，不同于字符串。 字符串就不能修改
    list5 = [1, 2, 3, 4]

    # 修改元素
    list5[0] = 6
    func(24, list5)

    #  添加元素（append向末尾添加元素）
    list5.append("hi")
    #list5.remove()
    func(25, list5)

    # insert方法添加元素
    list5.insert(0, 'our')
    func(26, list5)


    # 列表中同时追加多个元素
    list7 = [1, 2, 3, 4]
    b = ['a',100]
    list7.extend(b)
    func(27, list7)


    list8 = [1, 2, 3, 4]
    str1 = "hello"
    #list8.extend(str1)  #拆分
    list8.extend([str1])  # 作为一个元素
    func(28, list8)

    # 列表中删除元素，del、pop
    list9 = [1, 2, 3, 4]

    del list9[0]  # del删除，并不能使用变量接收删除的值
    func(29, list1)
    del list9[-1]
    func(30, list1)

    # 5、pop方法删除末尾元素，并接着使用这个元素，索引不能越界
    list10 = ['a', 'b', 'c', 'd']
    func(31, list10)

    # 5.1、pop_list1存储删除的元素
    pop_list1 = list10.pop()
    func(32, list10)
    func(33, pop_list1)

    # 5.2、pop(i)删除指定位置元素
    p_list1 = list10.pop(1)
    func(34, p_list1)

    # 5.3、根据值删除元素
    list11 = ['1', '2', '3', '2']
    list11.remove('2')  # 一次删除一个，前一个
    # list11.remove('20')  #如果不存在，则报错
    func(35, list11)

    # 清空列表clear
    list11.clear()
    func(36, list11)

    # 10、元组
    # 列表非常适合存储程序运行期间可能变化的数据集。
    # 不可变的列表称为元组,可作为字典的key
    tuple1 = (1, 2, 3)
    tuple2 = (1)
    tuple3 = (1,)  # 只有一个元素的元组

    func(37, type(tuple2))
    func(38, type(tuple3))
    func(39, tuple1[1])
    func(40, tuple1[::-1])
    func(41, tuple1.index(1))

    t = (1, 2, 3)
    a, b, c = t
    # a, b, c = (1, 2, 3)
    # a, b, c = 1, 2, 3
    func(42, f"t = {t} a = {a} b = {b} c = {c}")









    # 7、操作列表
    # 遍历列表(单复数有助于分辨是单个列表元素还是整个列表元素)
    # for 循环后面，没有缩进的代码都只执行一次，而且不会重复执行
    list_ones = ['java编程思想', 'Python从入门到精通', '数据结构', '人生苦短，我用Python']
    for list_one in list_ones:
        func(43, (list_one.title() + "\n"))
    func(44, "play now!")

    # 7.1、创建数值列表
    # 使用range函数,包头不包尾
    for value in range(1, 5):
        func(45, value)

    # 7.2、创建数字列表,使用list函数将range()结果直接转化为列表
    numbers = list(range(1, 6))
    func(46, numbers)

    # 7.3、指定步长(打印1到10以内的偶数)
    even_numbers = list(range(2, 11, 2))
    func(47, even_numbers)

    # 7.4、 将前10个整数的平方存到一个列表中
    squares = []
    for value in range(1, 11):
        squares.append(value ** 2)
    func(48, squares)

    # 8、列表解析(列表名，表达式，for循环)
    lists = [value ** 2 for value in range(1, 11)]
    func(49, lists)

    # 不可修改元组中元素，因此不能赋值
    # 10.1、遍历元组

    tuple3 = ('a','b','c')
    for b in tuple3:
        func(50, b)


demoList()
