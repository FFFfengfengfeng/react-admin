# -*- coding: UTF-8 -*-

# 斐波那契数列。

def fib(n):
    if n < 2:
        return n
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

print fib(10)