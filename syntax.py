# -*- coding: UTF-8 -*-
# python标识符由字母,数字,下划线组成,不能以下划线开头
# python标识符区分大小写
# 以下划线开头的标识符是有特殊意义,表示不能直接访问的类属性
# 以双下划线开头的标识符表示类的私有成员,以双下划线开头和结尾的标识符表示python里特殊方法专用的标识
# 一行可以有多条语句,用分号隔开

# 行和缩进
# python代码块不使用尖构号来控制类,函数以及其他逻辑判断,python是以缩进进行判断

# 多行语句
# python中可以用\将一行语句分为多行

# python中可以使用单引号,双引号,三引号来表示字符串,其中三引号可以编写多行文本
# python中的注释用#号开头

# raw_input("按下enter键退出")

x = "a"
y = "b"

print x,
print y,

print '----'

print x
print y

#python中的语句

conditions = True

if conditions:
    print "conditions为true"
else:
    print "conditions为false"