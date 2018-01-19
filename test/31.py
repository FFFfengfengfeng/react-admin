# -*- coding: UTF-8 -*-

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

def decideWeek(string):
    # days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = {
        'm': '星期一',
        't': {
            'u': '星期二',
            'h': '星期四'
        },
        'w': '星期三',
        'f': '星期五',
        's': {
            'a': '星期六',
            'u': '星期六'
        }
    }
    if f.lower() in ['m', 'w', 'f']:
        print '这是星期%s' % days[f]
    elif f.lower() in ['t', 's']:
        s = raw_input('请输入第二个字母: ')
        print '这是星期%s' % days[f][s]
    else:
        print '请重新输入字母: '
#
f = raw_input('请输入字母: ')
decideWeek(f)



