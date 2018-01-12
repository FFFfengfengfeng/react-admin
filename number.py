# -*- coding: UTF-8 -*-
import math
import random

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

# exp(x)返回e的x次幂
print math.exp(3)

# fabs(x)返回数字x的绝对值
print math.fabs(-2)

# floor(x)向下取整
print math.floor(4.9)

# max(x1,x2,x3)返回给定参数的最大值,min(x1,x2,x3)用法一样
print max(3,4,5,2,7,2)
arr = [4, 2, 3, 1]
print max(arr)

# modf(x)返回x的整数部分和小数部分,两部分的数值符号与x相同
print math.modf(29.21)

# pow(x,y)返回x**y的结果
print pow(3, 2)

# round(x, [n])返回浮点数X的四舍五入值,n表示舍入的小数点位数
print round(3.22, 1)
print round(3.22, 2)
print round(5.48)
print round(1)

# sqrt(x)返回数字x的平方根
print math.sqrt(4)

# python随机函数
# 随机数可用于数字,游戏,安全等领域

# choice(eq)从序列中随机挑选一个元素
print random.choice(range(19))

# randrange ([start,] stop [,step])从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
print random.randrange(0, 100)

# random()随机生成下一个实数,在[0,1)之间
print random.random()

# seed()改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

# shuffle(lst)将序列的所有元素随机排序
arr = [4, 2, 3, 1]
random.shuffle(arr)
print arr

# uniform(x,y)随机生成下一个实数,他在[x,y]范围内
print random.uniform(4,4.5)

# python中的三角函数