# -*- coding: UTF-8 -*-
# python多线程
# 多线程类似于同时执行多个程序,多线程有以下有点:
# 使用线程可以把占据长时间的程序的任务放到后台处理
# 程序运行速度可能加快
# 在一些等待的任务上如用户输入,文字读写和网络收发数据等,现成比较有用

# python使用线程有两种方式: 函数或者用类来包装线程对象
# 函数式,调用thread模块中的start_new_thread来产生新的线程
# start_new_thread(function, (参数))
# 实例

import thread
import time

# 定义线程函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s: %s' % (threadName, time.ctime(time.time()))

# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"
