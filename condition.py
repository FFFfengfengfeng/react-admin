# -*- coding: UTF-8 -*-

# python中的条件语句
# python中任何非0和非空的值都为true,0或者null都为false

# if 基本用法
flag = False
name = 'python'

if name == 'python':
    flag = True
    print 'hello python'
else:
    print 'hello world'

# elif 基本用法

num = 5

if num == 3:
    print '1'
elif num == 2:
    print '2'
elif num == 1:
    print '3'
else:
    print '4'

# if判断多个条件

num = 9
if num >= 0 and num <= 10:
    print '数字在0到10之间'

