import sys
import psutil  # 需要安装
import os
import gc


print(gc.get_count())
print(gc.get_threshold())

print('-----------------------sys.getrefcount() 获取引用的次数')
# sys.getrefcount()  # 获取引用的次数
a = []
print(sys.getrefcount(a))  # 两次
b = a
print(sys.getrefcount(a))  # 3次
d = b
e = b
print(sys.getrefcount(a))  # 5次

print('-----------------------验证循环引用的情况 ')
def showMemSize(tag):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{} memory user: {} MB'.format(tag, memory))
    pass


# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象 a b 之后')
    # print(sys.getrefcount(a))  # 获取引用的次数
    # print(sys.getrefcount(b))

    del a   # 删除对象
    del b
    pass


func()
gc.collect() # 手动 释放
showMemSize('完成后的时候：')
print('-----------------------gc模块 ')

print(gc.get_count())
print(gc.get_threshold())