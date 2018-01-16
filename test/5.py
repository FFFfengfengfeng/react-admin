# -*- coding: UTF-8 -*-

# 输入三个整数x,y,z，请把这三个数由小到大输出。

num1 = input('请输入一个正整数: ')
num2 = input('请输入一个正整数: ')
num3 = input('请输入一个正整数: ')
lists = []
lists.append(num1)
lists.append(num2)
lists.append(num3)

lists.sort()

print lists