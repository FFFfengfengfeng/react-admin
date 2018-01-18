# -*- coding: UTF-8 -*-

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

num = input('请输入数字: ')
times = input('请输入相加次数: ')

lists = []
for i in range(1, times):
    if i == 1:
        lists.append(num)
    else:
        lists.append(10 ** (i - 1) * num)
        lists[len(lists) - 1] = lists[len(lists) - 1] + lists[len(lists) - 2]

result = 0
for i in range(len(lists)):
    result += lists[i]

print '结果是: ', result