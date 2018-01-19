# -*- coding: UTF-8 -*-

# 题目：按相反的顺序输出列表的值。

list1 = [1, 2, 3, 4, 5, 6]

i = len(list1)
while i > 0:
    print list1[i - 1]
    i -= 1
