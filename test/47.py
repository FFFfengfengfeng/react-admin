# -*- coding: UTF-8 -*-

# 题目：两个变量值互换。

def exchange(a , b):
    a, b = b, a
    return (a, b)

a = 1
b = 2
print exchange(a, b)