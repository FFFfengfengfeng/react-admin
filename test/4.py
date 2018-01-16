# -*- coding: UTF-8 -*-

# 输入某年某月某日，判断这一天是这一年的第几天？

import calendar

year = input('请输入年: ')
month = input('请输入月: ')
day = input('请输入日: ')

days = 0

for i in range(0, month - 1):
    days += calendar.monthrange(year, i + 1)[1]

print '%d年%d月%d日' % (year, month, day),'这一天是这一年的第',days + day,'天'