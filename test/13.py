# -*- coding: UTF-8 -*-

# 题目：打印出1000以内所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

result = []
for i in range(100, 1000):
    bai = i / 100
    tens = i % 100 / 10
    bit = i % 10
    if bai ** 3 + tens ** 3 + bit ** 3 == i:
        result.append(i)

print result