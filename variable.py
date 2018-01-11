# -*- coding: UTF-8 -*-

# 变量赋值,python中的变量复制不需要声明类型

# 整型变量
counter = 100
# 浮点型
miles = 1000.0
# 字符串类型
name = "John"

print counter
print miles
print name

# 多个变量复制

a = b = c = 1

print a,
print b,
print c,

# python中有5个标准数据类型
# Numbers
# String
# List
# Tuple
# Dictionary

num1 = 1
# del可以删除对象

# python中的字符串
s = "ilovepython"
# 字符串切割
print s[1:5]
# +号表示字符串拼接,*号表示重复操作
str1 = 'hello world'
print str1[0]
print str1[2:5]
print str1 + '222'
print str1 * 2

# python中的列表
list1 = ['abc', 123, 2.23, 'john']
list2 = [123, 'john']

print list1
print list1[0]
print list1[1:3]
print list1[1:]
print list1 + list2

print '-----------------'
# python中的元祖
# 元祖不能二次复制,相当于只读的list
tuple1 = ('abc', 1234, 'john', 20)
tuple2 = (123, 'john')

print tuple1
print tuple1[0]
print tuple1[1:3]
print tuple2 * 2
print tuple1 + tuple2

# python中的字典
