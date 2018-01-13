# -*- coding: UTF-8 -*-

# python中的模块,是一个python文件,以.py结尾,包含了python对象定义和python语句
# 模块让你能够有逻辑地组织你的python代码

# 实现一个简单的模块
def print_hi( par ):
    print 'Hello : ', par
    return

# 引入模块的语法import module1
# import tool
#
# result = tool.sum_total(1, 2, 4)
# print result

# from...import语句
# 使用from语句可以从模块中导入一部分函数到当前命名空间中

from tool import sum_total
print sum_total(1, 2, 3)

# 当导入一个模块的时候,python解析器对模块位置的顺序是:
# 1.当前目录
# 2.如果不在当前目录,python则搜索shell变量PYTHONPATH下的每个目录
# 3.如果都找不到,python会察看默认路径

# 命名空间和作用域

price = 1
def add_price():
    global price
    price += 1
add_price()
print price

# dir()函数是一个排好序的字符串序列,内容是一个模块里定义的名字
# 返回的列表容纳了在一个模块里定义的所有模块,变量,函数
# 实例
import math

content = dir(math)

print content
print '----------------'

# globals()和locals()函数
# 根据调用地方的不同,globals()和locals()函数可以返回全局和局部命名空间里的名字
# 如果在函数内使用locals()返回的是所有能在该函数里访问的命名
# 如果在函数内调用globals()返回的是所有能在改函数访问的全局名字

def test_global():
    glo = globals()
    loc = locals()
    print glo
    print '-------------------'
    print loc
test_global()

# reload()函数
# 当一个模块被导入到一个脚本,模块顶层部分的代码只会被执行一次。
# 因此,如果你想重新执行模块里顶层部分的代码,可以用reload()函数,该函数会重新导入之前的模块
# 语法reload(模块名)

# python中的包
# 包是一个分层次的文件目录结构,它定义了一个由模块及子包,和子包下的子包等组成的python的应用环境
#