# !/usr/bin/env python
# -*- coding:utf-8 -*-


#
# def get_populuation(country):
# 	return country[2] #即按popu排序

countries = []
file = open("/Users/sudo/Documents/dataset/dataset-master/country/countries_zh.csv","r")
for line in file:
	line = line.strip()
	arr = line.split(",")
	name = arr[1]
	capt = arr[3]
	popu = int(arr[4])
	countries.append((name,capt,popu))
# countries.sort()
"""
需求：根据人口排序
"""
# countries.sort(key=get_populuation)
countries.sort(key=lambda country: country[2])
for country in countries:
	print(country)

