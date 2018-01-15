# -*- coding: UTF-8 -*-
# encoding: utf-8
# python标准数据库接口为Python DB-API

import MySQLdb

db = MySQLdb.connect('127.0.0.1', 'root', '', 'sale', charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

try:
    cursor.execute('select * from company')
    results = cursor.fetchall()
    for row in results:
        print '名字: ', row[1], ' 规模: ', row[0]
except:
    print 'Error: unable to fecth data'
# 关闭数据库连接
db.close()