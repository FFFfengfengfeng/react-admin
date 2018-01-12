# -*- coding: UTF-8 -*-

# python能有很多方式处理日期和时间,转换日期格式是一个常见的功能
# time模块和calendar模块可以用于格式化日期和时间

import time

ticks = time.time()
print '当前的时间戳:' , ticks

# 时间元组

local = time.localtime(time.time())
print local

# asctime()获取格式化的时间