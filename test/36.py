# -*- coding: UTF-8 -*-

# 题目：求100之内的素数。

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

result = []

for i in range(1, 101):
    if isPrime(i):
        result.append(i)

print result
print '100以内的素数个数是: %d' % len(result)