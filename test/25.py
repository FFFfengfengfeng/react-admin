# -*- coding: UTF-8 -*-

# 题目：求1+2!+3!+...+20!的和。

def factorial(n):
    sum = 1
    for i in range(n):
        sum *= (n - i)
    return sum

sum = 0
for i in range(20):
    sum += factorial(i + 1)

print sum
