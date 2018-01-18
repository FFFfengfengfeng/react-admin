# -*- coding: UTF-8 -*-

# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

reboundHeight = []

for i in range(1, 12):
    reboundHeight.append(100 * (0.5 ** (i - 1)))

print reboundHeight

print '第10次反弹高度: ', reboundHeight[10]

totalHeight = 0
for i in range(len(reboundHeight) - 1 ):
    if i == 0:
        totalHeight += reboundHeight[i]
    else:
        totalHeight += reboundHeight[i] * 2
print '经过了:', totalHeight, '米'