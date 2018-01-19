# -*- coding: UTF-8 -*-

# 题目：利用递归方法求5!

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

print factorial(5)