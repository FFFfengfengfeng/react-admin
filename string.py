# -*- coding: UTF-8 -*-

# 字符串是python中最常用的数据类型

# 创建字符串
str1 = 'hello world'

print str1[2 : 5]

print str1[: 3] + '111'

# python中的字符串运算符

# + 字符串连接
str1 = 'hello'
str2 = 'world'

print str1 + str2

# * 重复输出字符串
str1 = 'F'
print str1 * 5

# 通过索引获取字符串
str1 = 'dasdsad'
print str1[1]

# [:]对数组进行截取
str1 = 'Hello'
str2 = str1[0:2]

print str1, str2

# in 成员运算符
str1 = 'hello'
print 'h' in str1
print 'z' in str1

print r'\n'

# % 字符串格式化
print 'my name is %s and my age is %d' % ('FFF', 26)

# count 统计字母出现次数
str1 = 'hello'
print str1.count('l', 0, len(str1))