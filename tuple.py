# -*- coding: UTF-8 -*-

# python中的元组与列表相似,但元组中的元素是不能修改

tuple1 = (1, 2, 3, 4, 5)

tuple1 = (1,)
tuple2 = (1, 2, 3, 4, 5)

print tuple1[0]
print tuple2[2: 4]

# 元组是不可修改的,但可以创建新的元组进行连接

tuple1 = (1, 2, 3)
tuple2 = (4, 5)

tuple3 = tuple1 + tuple2
print tuple3

# 元组的元素是不可删除的,但可以删除整个元组
tup = ('physics', 'chemistry', 1997, 2000)
del tup