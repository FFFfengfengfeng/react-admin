# -*- coding: UTF-8 -*-

# python中的列表相当于js的数组

list1 = ['physics', 'chemistry', 1997, 2000]

print list1[1]

list1[1] = '111'

print list1

del list1[1]

print list1

# python中的列表方法
# cmp(list1, list2)比较两个列表中的元素
str1 = [1, 2, 3, 4]
str2 = [2, 3]

str3 = ['FFF', 'EEE']
str4 = ['QQQ', 'JJJ']
# 返回值
# 如果比较的元素是同类型,则比较其值,返回结果
# 如果两个元素不是同数据类型,则检查他们是否是数字
#   如果是数字,执行必要的数字强制类型转换,然后比较
#   如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
#   否则,通过类型名字的字母顺序进行比较
# 如果有一个列表首先到达末尾,则另一个长一点的列表"大"
# 如果所有比较结果的元素都是相等,则返回0
print cmp(str3, str4)

# append()向列表末尾添加元素
str1 = [1, 2, 3, 4]
str1.append(5)
print str1

# count()计算某个元素在list中出现的次数
print str1.count(1)

# extend()在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 没有返回,但会在原数组中添加元素
str1 = [1, 2, 3, 4, 5]
str2 = [6, 7, 8]
str1.extend(str2)
print str1

# index()从列表中找出某个值第一个匹配项的索引位置
nums = [2, 2, 1, 3, 4]
index = nums.index(1)
print index

# insert()将对象插入列表
books = [
    {
        'name': '水浒传',
        'author': '施耐庵'
    },
    {
        'name': '红楼梦',
        'author': '曹雪芹'
    },
    {
        'name': '三国演义',
        'author': '罗贯中'
    },
    {
        'name': '西游记',
        'author': '吴承恩'
    }
]
books.insert(3, {
    'name': '骆驼祥子',
    'author': '老舍'
})
print books

for i in range(len(books)):
    print '书名: ', books[i]['name'], '作者: ', books[i]['author']

# pop()移除列表中的一个元素,并且返回该元素的值
# 默认是最后一个元素,可以将下标作为参数
print '--------------------'
current = books.pop(0)
for i in range(len(books)):
    print '书名: ', books[i]['name'], '作者: ', books[i]['author']

# remove()移除列表中某个值的第一个匹配项
nums = [1, 2, 3, 4, 5]
nums.remove(2)
print nums

# reverse()反向列表中的元素
nums = [1, 2, 3, 4, 5]
nums.reverse()
print nums

# sort()对原数组进行排序
nums.sort()
print nums

