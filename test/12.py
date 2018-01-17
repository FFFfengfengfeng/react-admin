# -*- coding: UTF-8 -*-

# 题目：判断101-200之间有多少个素数，并输出所有素数。

# 定义函数判断一个数字是否是素数
import math
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print isPrime(125)

result = []
# 循环判断101-200中的素数
for i in range(101, 200):
    flag = isPrime(i)
    if flag:
        result.append(i)
    else:
        continue

print result
print '101-200之间的素数有: ', len(result), '个'

