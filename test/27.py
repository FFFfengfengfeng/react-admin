# -*- coding: UTF-8 -*-

# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def reversal(n, str):
    if n == 0:
        return str[0]
    else:
        return str[n] + reversal(n - 1, str)

str = 'hello'

print reversal(len(str) - 1, str)
