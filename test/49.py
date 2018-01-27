# -*- coding: UTF-8 -*-

# 题目：使用lambda来创建匿名函数。

MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y

a = 10
b = 20
print 'The largar one is %d' % MAXIMUM(a,b)
