# -*- coding: UTF-8 -*-

# 题目：打印出如下图案（菱形)

for j in range(0, 7):
    if j <= 3:
        print ' ' * (3 - j), '*' * (j * 2 + 1)
    else:
        print ' ' * (j - 3), '*' * (13 - 2 * j)