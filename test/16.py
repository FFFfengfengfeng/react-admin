# -*- coding: UTF-8 -*-

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

str = raw_input('请输入一行字符: ')

letters = []
spaces = []
digits = []
others = []

for i in str:
    if i.isspace():
        spaces.append(i)
    elif i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        others.append(i)

print '数字: %d个, 字母: %d个, 空格: %d个, 其他: %d个' % (len(digits), len(letters), len(spaces), len(others))