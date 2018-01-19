# -*- coding: UTF-8 -*-

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

import operator

def printNum(num):
    str1 = str(num)
    print '这是一个%s位数' % len(str1)
    result = []
    for i in range(0, len(str1)):
        result.insert(0, str1[i])
    print ''.join(result)
printNum(189)