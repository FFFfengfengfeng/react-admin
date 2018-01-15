# -*- coding: UTF-8 -*-

# python中的正则表达式
# python中的re模块可以实现python中的正则表达式操作

import re

# match尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,match()就返回none
# re.match(pattern, string, flags=0)
# pattern 匹配的正则表达式
# string  匹配的字符串
# flags   标志位,如是否多行匹配,区分大小写等
# 如果匹配成功则返回对象,否则返回none

# group()方法匹配整个表达式的字符串,group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()方法返回一个包含所有小组字符串的元组

# 实例

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

# re.search方法
# 返回成功匹配的第一个

print re.search('www', 'www.runoob.com').span()

# re.sub可以用于检索和替换
phone = '2004-959-559 # 这是一个国外电话号码'

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', '', phone)
print '电话号码是: ', num

# 删除(-)
nums = re.sub(r'-', '', num)
print '电话号码是: ', nums

# 实例: 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))