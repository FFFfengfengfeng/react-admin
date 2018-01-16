# -*- coding: UTF-8 -*-

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

profit = input('请输入利润(万元)')
bonus = 0
if profit <= 10:
    bonus = profit * 0.1
elif profit > 10 and profit < 20:
    bonus = 1 + (profit - 10) * 0.075
elif profit >= 20 and profit < 40:
    bonus = 1 + 0.75 + (profit - 20) * 0.05
elif profit >= 40 and profit < 60:
    bonus = 1 + 0.75 + 1 + (profit - 40) * 0.03
elif profit >= 60 and profit < 100:
    bonus = 1 + 0.75 + 1 + 0.6 + (profit - 60) * 0.015
elif profit > 100:
    bonus = 1 + 0.75 + 1 + 0.6 + 0.6 + (profit - 100) * 0.01

print bonus