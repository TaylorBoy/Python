#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, queue, time
from multiprocessing.managers import BaseManager

# 1. 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 2. 注册, 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 3. 连接到服务器, 即master的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
#    端口和验证码注意保持与task_master.py设置的完全一致
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')
#    从网络连接
manager.connect()
# 4. 获取Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 6. 从task队列获取结果
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print('Run task %d * %d...' %(n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Queue().Empty:
        print('Task queue is empty.')

print('*** Done ***')
