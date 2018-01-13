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

