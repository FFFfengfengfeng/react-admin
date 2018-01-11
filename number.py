# -*- coding: UTF-8 -*-
import math

# python中的数字
# python的number数据类型用于存储数值
# 数据类型在python中是不允许改变的,意味着改变number的值,将重新分配内存

# 创建number的实例
num1 = 2
num2 = 3

# 删除number的实例
del num1

# print num1 报错

# python支持四种不同类型的数值类型
# 整型int 整数,不带小数点
# 长整型long 无限大小的整数,整数最后一位是一个大写或小写的L
# 浮点型float 小数
# 复数

# python中的数学函数

# abs(x)返回数字的绝对值
a = -2
print abs(a)

# ceil(x)向上取整
a = 4.1
print math.ceil(4.1)

# cmp(x, y)如果x < y返回-1, 如果x == y返回0, 如果x > y返回1
x = 5
y = 2
z = 2
print cmp(x, y)
print cmp(z, y)
print cmp(y, x)