# -*- coding: UTF-8 -*-

# python中的循环语句
# while循环
# for循环
# 嵌套循环

# 循环控制语句
# break语句
# continue语句
# pass语句

# while 基本用法1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

while len(nums) > 0:
    num = nums.pop()
    if (num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)

print even
print odd

# while 基本用法2
score = [40, 50, 60, 80, 90, 35, 95]
count = 0
sum = 0
while count < len(score):
    sum += score[count]
    count += 1

print '平均分: ', sum / len(score)

# continue 和 break的用法
# 计算1000以内的水仙花数

count = 3
result = []
while count < 1000:
    hundreds = count / 100
    tens = count % 100 / 10
    ones = count % 100 % 10
    if (hundreds > 0):
        if ((hundreds ** 3 + tens ** 3 + ones ** 3) == count):
            result.append(count)
    elif (tens > 0):
        if ((tens ** 2 + ones ** 2) == count):
            result.append(count)
    elif (ones ** 1) == count:
        result.append(count)
    count += 1

print result

# 计算100以内的双数

count = 0
result = []

while count < 100:
    count += 1
    if ( count % 2 > 0 ):
        continue
    else:
        result.append(count)
else:
    print '循环结束了'
print result

# for 循环语句
# for 循环简单使用

for item in 'python':
    print '当前字母:', item

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

for i in range(len(books)):
    print '书名: ', books[i]['name'], '作者: ', books[i]['author']

# 嵌套循环
# 冒泡排序

nums = [20, 40, 60, 80, 30, 70, 90, 10, 50, 0]
i = 0
j = 0


while i < len(nums):
    i += 1
    while j < i - 1:

        if (nums[j] > nums[j + 1]):
            cache = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = cache

        j += 1

print nums

# break语句
# break实例

for item in 'python':
    if item == 'o':
        break
    print '当前字母: ', item

# 第二个实例
count = 0
while count < 10:
    if count == 5:
        break
    print count
    count += 1

# continue语句
# continue实例

#输出100以内的双数和
sum = 0
count = 0

while count < 100:
    count += 1
    if (count % 2 > 0):
        continue
    else:
        sum += count
print sum

# 输出三角形

i = 0
j = 0

while i < 4:
    while j < 4:
        print ' ' * (3 - j), '*' * (2 * i + 1)
        i += 1
        j += 1
