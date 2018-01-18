# -*- coding: UTF-8 -*-

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def reviewScore(score):
    if score >= 90:
        return 'A'
    elif score > 60 and score <= 89:
        return 'B'
    else:
        return 'C'

score = input('请输入分数: ')
grade = reviewScore(score)
print grade
print '%d分属于%s' % (score, grade)