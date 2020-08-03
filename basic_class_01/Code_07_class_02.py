# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 继承
class Person():
    def talk(self):
        print("talking...")

class Chinese(Person):
    def walk(self):
        print("walking...")

obj = Chinese()
obj.talk()
obj.walk()