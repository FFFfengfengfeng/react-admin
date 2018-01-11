# -*- coding: UTF-8 -*-

# python中的运算符
# 算术运算符
# 比较（关系）运算符
# 赋值运算符
# 逻辑运算符
# 位运算符
# 成员运算符
# 身份运算符
# 运算符优先级

a = 21
b = 10
c = 0

c = a + b
print 'a + b = ', c

c = a - b
print 'a - b = ', c

c = a * b
print 'a * b = ', c

c = a / b
print 'a / b = ', c

c = a % b
print 'a % b = ', c

# 修改变量 a, b, c
a = 2
b = 3
c = a**b
print 'a**b = ', c

# //整除,返回商的部分
a = 10
b = 5
c = a // b
print 'a // b = ', c

a = 3
b = 2
print 'a / b = ', a / b
print '(带小数)a / b = ', a / float(b)

# python中的比较运算符
# == 等于-比较对象是否相等
# != 不等于-比较两个对象是否不相等
# <> 不等于-比较两个对象是否不相等
# >  大于-返回X是否大于Y
# <  小于-返回X是否小于Y,比较运算符返回1表示真,返回0表示假
# >= 大于等于-返回X是否大于等于Y
# <= 小于等于-返回X是否小于等于Y

print '----------------'

a = 21
b = 10
c = 0

if ( a == b ):
    print 'a等于b'
else:
    print 'a不等于b'

if ( a != b ):
    print 'a不等于b'
else:
    print 'a等于b'

if ( a <> b ):
    print 'a不等于b'
else:
    print 'a等于b'

if ( a > b ):
    print 'a大于b'
else:
    print 'a不大于b'

if ( a < b ):
    print 'a小于b'
else:
    print 'a不小于b'

if ( a >= b):
    print 'a大于等于b'
else:
    print 'a小于b'

if ( a <= b ):
    print 'a小于等于b'
else:
    print 'a大于b'

# python中的赋值运算符
# =   简单的复制运算
# +=  加等于
# -=  减等于
# *=  乘等于
# /=  除等于
# %=  取模赋值运算
# **= 幂赋值运算
# //= 取整除赋值运算

a = 21
b = 10
c = 0

c += a
print 'c += a:', c

c *= a
print 'c *= a:', c

c /= a
print 'c /= a:', c

c = 2
c %= a
print 'c %= a:', c

c **= a
print 'c **= a:', c

c //= a
print 'c //= a:', c

# python中的位运算
# &按位与运算符,如果两个相应位都为1,则为1,否则为0
# |按位或运算符,如果两个相应位都为0,则为0,否则为1
# ^按位异或运算,如果两个相应位相异时,结果为1
# ~按位取反
# <<左移运算,
# >>右移运算

a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101

c = 0

print 'a & b:', a & b

print 'a | b:', a | b

print 'a ^ b:', a ^ b

print '~ a:', ~ a

print 'a << 2:', a << 2

print 'a >> 2:', a >> 2

# python中的逻辑运算符
# and 与
# or  或
# not 非

a = 10
b = 20

if ( a and b ):
    print 'a和b都为true'
else:
    print 'a和b不同为真'

if ( a or b ):
    print 'a或者b至少有一个为真'
else:
    print 'a和b都为假'

if not( a and b ):
    print 'a和b不全是真'
else:
    print 'a和b都是真'

# python中的成员运算符
# in     如果在指定序列中找到值返回true,否则返回false
# not in 如果在指定的序列找不到改值返回true,否则返回false

a = 10
b = 20

list1 = [1, 2, 3, 4, 5]

if ( a in list1 ):
    print 'a在list1中'
else:
    print 'a不在list1中'

if ( b not in list1 ):
    print 'b不在list1中'
else:
    print 'b在list1中'

# python中的身份运算符
# is     判断两个标识符是不是引用同一个对象
# is not 判断两个标识符是不是引用不同的对象

a = 20
b = 20

if ( a is b ):
    print 'a和b有相同的标识'
else:
    print 'a和b没有相同的标识'

b = 30

if ( a is not b ):
    print 'a和b没有相同的标识'
else:
    print 'a和b有相同的标识'