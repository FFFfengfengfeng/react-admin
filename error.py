# -*- coding: UTF-8 -*-

# python异常处理
# 实例

try:
    fo = open('FFF.txt', 'w')
    fo.write('Hello World')
except IOError:
    print 'Error: 没有找到该文件'
else:
    print '写入成功'
    fo.close()