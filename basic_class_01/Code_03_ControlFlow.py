# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))
    #print('{0}, {1}' .format(index, obj))



# 控制流
def demoControlFlow():

    score = 66

    # if/else
    if score % 2 == 0:
        #func(0, "{0}这个数是偶数".format(score))
        func(0, (str)(score)+"这个数是偶数")
        if score % 3 == 0:
            func(0, "{0}这个数还能被3整除".format(score))
    else:
        func(1, "{0}这个数是奇数".format(score))

    # if/elif else 额外条件判断
    #特别注意：空字符串 ""、0、None、空对象，都当作False来处理
    if score > 80:
        func(2, "A")
    elif score > 60:
        func(3, "B")
    else:
        func(4, "C")

    # for循环,可遍历列表，字符串，元组、range
    for i in range(0, 4):
        if i == 2:
            continue  # continue 单次循环先结束
       # if i == 1:
       #    break  # break 整个循环结束

        func(5, i)

    # for循环
    vals = "abc"
    for val in vals:
        func(6, val)


    # while 知道循环结束条件
    target = 3
    current = 1
    while current < target:
        current += 1
    func(7, current)

    #pass 占位符
    for i in range(5):
        pass

demoControlFlow()
