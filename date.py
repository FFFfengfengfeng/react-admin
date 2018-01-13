# -*- coding: UTF-8 -*-

# python能有很多方式处理日期和时间,转换日期格式是一个常见的功能
# time模块和calendar模块可以用于格式化日期和时间

import time
import calendar

ticks = time.time()
print '当前的时间戳:' , ticks

# 时间元组

local = time.localtime(time.time())
print local

# asctime()获取格式化的时间
local = time.asctime(time.localtime(time.time()))
print local

# strftime()格式化日期
# local = time.strftime("%Y-%m-%d %H:%M:%s", time.localtime())
local = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print local

# 获取日历
cal = calendar.month(2016, 1)
print '以下输出2016年1月份的日历:'
print cal