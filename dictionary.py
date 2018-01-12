# -*- coding: UTF-8 -*-

# python中的字典是一种存储任意类型的对象,字典中的每个键值(key=>value)对用冒号(:)分割,每个对之间用逗号(,)分割
# 键值是必须的,但值则不是必须的
# 一个简单的字典类型
dict = {
    'name': 'henry',
    'age': '24',
}

print dict

# 访问字典中的值
print dict['name']

# 修改字典
dict['name'] = 'FFF'
print dict

# 字典能删除也可以清空
# 删除字典的元素
del dict['name']
print dict
dict['name'] = 'FFF'
print dict
# dict.clear()
# print dict

# 字典键的特性
# 字典的值可以取任意的python对象,但键有限制的条件
#  不允许同一个键出现两次,同一个键被赋值两次,将会覆盖

# 内置函数
# clear()删除字典的所有元素

# copy()返回字典的一个浅复制
dict = {
    'name': 'henry',
    'age': '24',
}

dict1 = dict.copy()

print dict, '-------------'
dict1['name'] = 'FFF'
print dict1
print '-------------------'
# fromkeys()用于创建一个新的字典,以序列中的元素做字典的键,value为字典所有键对应的初始值
tuple1 = ('name', 'sex', 'age')
dict1 = dict1.fromkeys(tuple1)

print dict1

# get()返回指定键的值,不存在则返回默认值
dict = {
    'name': 'henry',
    'age': '24',
}
name = dict.get('sex')
print name

# has_key()判断改字典是否含有该Key
dict = {
    'name': 'henry',
    'age': '24',
}
flag = dict.has_key('name')
print flag

# items()以列表返回可遍历的(键,值)元组数组
dict = {
    'name': 'henry',
    'age': '24',
}

print dict.items()

# keys()以列表返回一个字典的所有键
dict = {
    'name': 'henry',
    'age': '24',
}
print dict.keys()

# setdefault()与key()相似,但找不到该键,将会添加到字典
dict = {
    'name': 'henry',
    'age': '24',
}
dict.setdefault('sex')
print dict

# dict.update(dict2)把字典dict2的键/值对更新到dict里
dict = {
    'name': 'henry',
    'age': '24',
}
dict2 = {
    'sex': '132'
}
dict.update(dict2)
print dict

# popitem()随机删除一对键值并返回