# -*- coding: UTF-8 -*-

# 题目：将一个数组逆序输出。

a = [1, 2, 3, 4, 5, 6]
b = []
for i in range(len(a)):
    b.insert(0, a[i])

print b