# -*- coding: UTF-8 -*-

# 题目：输出 9*9 乘法口诀表。

for i in range(1, 10):
    for j in range(1, i + 1):
        if i * j < 10:
            if i == j:
                print '%d x %d' % (j, i), '=', i * j, ' '
            else:
                print '%d x %d' % (j, i), '=', i * j, ' ',
        else:
            if i == j:
                print '%d x %d' % (j, i), '=', i * j, ''
            else:
                print '%d x %d' % (j, i), '=', i * j, '',