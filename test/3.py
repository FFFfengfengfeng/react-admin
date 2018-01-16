# -*- coding: UTF-8 -*-

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 完全平方数指一个整数是某个整数的完全平方

import math

result = []
for i in range(1, 168):
    if 168 % i == 0:
        result.append(i)

print result
m = 0
n = 0
for i in range(len(result)):
    for j in range(len(result)):
        if i * j != 168:
            continue
        else:
            m = (i + j) / 2
            if (i > j):
                n = i - m
            else:
                n = j - m

print m,n
print '这个整数是: ', 13 ** 2 - 268