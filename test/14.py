# -*- coding: UTF-8 -*-

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# num = input('请输入一个正整数: ')
import math
def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % 2 == 0:
                return False
        return True

def primeFactorization(n):
    flag = isPrime(n)
    if flag:
        print n, '= 1 *', n
        

primeFactorization(3)