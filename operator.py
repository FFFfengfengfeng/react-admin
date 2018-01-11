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