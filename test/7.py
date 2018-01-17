# -*- coding: UTF-8 -*-

# 将一个列表的数据复制到另一个列表中。

list1 = [1, 2, 3, 4, 5]
list2 = list1[0: len(list1)]

print list1
list2[0] = 0
print list1

