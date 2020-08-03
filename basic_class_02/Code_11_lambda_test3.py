# !/usr/bin/env python
# -*- coding:utf-8 -*-

def quadratic(a,b,c) :
	return lambda x:a*x*x +b*x +c
f = quadratic(1,-1,2)

# print(f(5))
print(quadratic(1,-1,2)(5))