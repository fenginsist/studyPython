import os
import shutil

print('---------------- 文件的 操作')
# 先手动创建一个  test.txt 文件
# os.rename('test.txt', 'myTest.txt') # 重命名
# os.remove('myTest.txt') # 删除文件，前提是文件必须存在，不存在删除则报错

print('---------------- 目录 的 操作')
# 创建目录
# os.mkdir('test')  # 只能创建一级目录，不能创建多级目录

# 创建多级目录
# os.makedirs('test/mytest') # 创建多级目录

# 更改名称
# os.rename('test', 'myTest')

# 删除目录
# os.rmdir('myTest')  # 只能删除空目录

# 如果要删除 非空目录的话， 就要导入shutil 模块 ，实现多级删除
# shutil.rmtree('myTest')

# 获取当前目录
print('当前目录：', os.getcwd())

# 路径的拼接
print(os.path) # <module 'ntpath' from 'D:\\devApp\\python\\lib\\ntpath.py'>
print(os.path.join(os.getcwd(), 'venv'))

# 目录的遍历
lista = os.listdir('D:\\Users\\Python\\StudyPython\\study09_file')
# print(lista)  # 返回的是一个列表    返回的一级目录
for dirname in lista:
    print(dirname)
    pass
print()
# 使用现代版 写法
# scandir 和 with一起来使用  这样的话 上下文管理器会在迭代器遍历完成后自动  去释放资源
with os.scandir('D:\\Users\\Python\\StudyPython\\study09_file') as entries:
    for entry in entries:
        print(entry.name)
        pass
    pass

# 仅遍历 文件 或者 目录
print()
basePath='d:/'
for entry in os.listdir(basePath):
    # if os.path.isfile(os.path.join(basePath,entry)):
    #     print(entry)
    if os.path.isdir(os.path.join(basePath,entry)):
        print(entry)
        pass
