# -*- coding: UTF-8 -*-
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

nums = [1, 2, 3, 4]
result = []
for i in range( len( nums ) ):
    for j in range( len( nums ) ):
        for k in range( len( nums ) ):
            if nums[i] <> nums[j] and nums[i] <> nums[k] and nums[j] <> nums[k]:
                a = nums[i] * 100
                b = nums[j] * 10
                num = a + b + nums[k]
                result.append(num)

print '可以组成: ', len(result), '个三位数'
print '分别是: ', result

