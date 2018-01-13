# -*- coding: UTF-8 -*-

# 函数是组织好的,可复用的,用来实现单一,或相关功能的代码段
# python定义函数以def开头,函数名括号

# 实例
def say_hi(name):
    return 'hello' + name

print say_hi('FFF')

# 可更改的类型和不可更改的类型
# python中string,tuples和numbers是不可更改的对象,而list和dict是可以更改的对象
# python函数的参数传递
# 参数的类型是不可更改的对象,在函数内部更改值相当于复制一个另一个对象不会应该改对象本身

a = 2

def add(num):
    num += 1
    return num
print a
print add(a)
print a

# 可变类型,当函数内部修改了该对象,list,dict,改对象外部也会修改

def filter(nums):
    for i in range(0, len(nums)):
        nums[i] *= 2
    return nums

nums = [1, 2, 3]
print nums
print filter(nums)
print nums

# 参数
# python的函数有四种参数类型
# 必备参数
# 关键字参数
# 默认参数
# 不定长的参数

# 必备参数
def say_hi(name):
    return 'hello' + name
# say_hi() 直接调用不传参数,将会报错

# 关键字参数
def compare(x, y):
    return x > y
# 关键字参数调用方式 compare(x = 2, y = 3)不需要按照参数声明的顺序调用
flag = compare(y = 3, x = 2)
print flag

# 缺省参数
# 声明的时候参数默认值
def info(name, age = 24):
    print name
    print age
    return
info('FFF')
info('DDD', 22)

# 不定长参数当参数不确定是使用
# 不定参数个数的实例
def add(*vartuple):
    result = 0
    for var in vartuple:
        result += var
    return result
print add(1, 2, 3)
print add(2, 3, 4, 5)

# 匿名函数
# python使用lambda来创建匿名函数

sum = lambda arg1, arg2 : arg1 + arg2
print sum(2, 3)

# return语句
def sum( *args ):
    total = 0
    for i in args:
        total += i
    return total
print sum( 1, 2, 3 )

# 变量作用域
# 全局作用域
# 局部作用域

# 全局变量和局部变量
# 定义在函数内部的变量就是局部变量
# 定义在全局的变量就是全局变量,整个程序的范围都可以访问
# 定义在函数内部的变量只能在变量内部访问
