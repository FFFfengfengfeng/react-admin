# -*- coding: UTF-8 -*-

# python 提供了两个级别访问的网络服务
# 低级别的网络服务支持基本的socket,它提供了标准的BSD Socket API, 可以访问底层操作Socket接口的全部方法
# 高级别的网络服务模块SocketServer,它提供了服务中心类,可以简化网络服务器的开发

# 使用socket方法创建socket
# AF_UNIX本机通信使用
# AF_INET跨机器之间使用
# socket对象内置方法

import socket

s = socket.socket()
host = socket.gethostname()
s.bind((host, 12345))

s.listen(5)

while True:
    c, addr = s.accept()
    print '111: ', addr
    c.send('222！')
    c.close()  # 关闭连接