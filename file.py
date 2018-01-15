# -*- coding: UTF-8 -*-
import os


# python 文件I/O操作

# 打印到屏幕使用print
print 'Hello World'

# 读取键盘输入
# raw_input
# input

# raw_input
# str = raw_input('请输入: ')
# print '你输入的内容: ', str

# input与raw_input用法一致,不过input可以接收一个表达式
# result = input('请输入: ')
# print '你输入的内容: ', result

# 打开和关闭文件
# python中可以使用file对象做大部分的文件操作

# open函数,使用open函数打开一个文件,创建一个file对象
# open(文件名, 模式, buff)
fo = open('foo.txt', 'wb')
print '文件名: ', fo.name
print '访问模式: ', fo.mode

#　close方法关闭该文件,禁止写入
# fo.close()

# read方法可以用于读取文件内容,write方法可以用于写入文件
# fo.open('foo.txt', 'wb')
fo.write('Hello World')

fo = open('foo.txt', 'r+')
str = fo.read()

print str

# 文件定位,tell方法可以获取文件的当前位置
position = fo.tell()
print '文件的位置: ', position
fo.close()

# 重命名和删除文件
# python的os模块提供了可以执行文件处理的方法
# 重命名rename方法
# os.rename('foo.txt', 'hello.txt')

# remove()方法可以删除文件
# os.remove('hello.txt')

# mkdir()可以创建新的目录
os.mkdir('FFF')

# chdir()方法来改变当前的目录
os.chdir('FFF')
print os.getcwd()
os.chdir('../')
# rmdir()方法可以删除目录
os.rmdir('FFF')
print os.getcwd()

# file对象常用函数
# file.close()用于关闭文件
# file.flush()用于刷新文件内部缓冲
# file.fileno()返回一个整型的文件描述符
# file.isatty如果文件连接到一个终端设备返回True,否则返回False
# file.next()返回下一行
# file.read()从文件读取指定的字节数,如果未给定或为负则读取所有
# file.readline()读取整行
# file.readlines()读取所有行并返回所有列
# file.seek()设置文件当前位置
# file.tell()返回文件当前位置
# file.truncate([size])截取文件,截取的字节通过size指定,默认当前文件位置
# file.write()将字符串写入文件,没有返回值
# file.writelines()向文件写入一个序列字符串

