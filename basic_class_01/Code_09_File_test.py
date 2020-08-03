# !/usr/bin/env python
# -*- coding:utf-8 -*-

def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 使用多个文件(重要)
x = ('This will build a very long long '
     'long long long long long long string')
def count_words(file):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file) as f1:
            contents = f1.read()
    except FileNotFoundError:
        msg = "sorry,the file " + file + " does not exist."
        func(1, msg)

    else:
        #split()可以指定分隔符，默认分隔符是任何空白字符
        words = contents.split()
        #for i in words:
        #   print("words文件中内容:"+i)
        num_words = len(words)
        func(2, ("The file " + file + " has about " + str(num_words) + " words."))


files = ['/Users/sudo/Documents/test_data/file.txt', '/Users/sudo/Documents/test_data/file1.txt', '/Users/sudo/Documents/test_data/file2.txt']
for file in files:
    count_words(file)
