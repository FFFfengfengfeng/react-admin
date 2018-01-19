# -*- coding: UTF-8 -*-

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# 分母
denominator = []
# 分子
numerator = []
sum = 0

for i in range(20):
    if i < 1:
        denominator.append(i + 1.0)
        numerator.append(i + 2.0)
    else:
        denominator.append(numerator[i - 1])
        numerator.append(numerator[i - 1] + denominator[i - 1])
    sum += float(numerator[i] / denominator[i])

print sum
