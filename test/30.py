# -*- coding: UTF-8 -*-

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def isPalindrome(string):
    arr = []
    for i in range(len(string)):
        arr.insert(0, string[i])
    if ''.join(arr) == string:
        return True
    else:
        return False

print isPalindrome('abcba')