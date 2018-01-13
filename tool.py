# -*- coding: UTF-8 -*-
# 测试模块导入

# 定义一个叠加函数
def sum_total(*nums):
    total = 0
    for i in nums:
        total += i
    return total
