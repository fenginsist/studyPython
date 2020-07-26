# 文件的操作
# 打开文件 open

# 复习：  \r：换行    \n:回车


# 默认的编码是 gbk 这个是中文编码，最好的习惯呢就是我们再打开一个文件的时候
# 给它指定一个编码类型  W
fobj = open('test.txt', 'w')  # 如果文件不存在，会自动创建
# 开始操作  读写操作
fobj.write('hello python 在苍茫的大海上\r\n')
fobj.write('狂风卷积着乌云\r\n')
fobj.close()  # 上面仅仅是写到内存中，使用close 写到磁盘中

# 以二进制的形式写数据
fobj2 = open('test2.txt', 'wb')  # str  --> bytes   a:用于追加
fobj2.write('在乌云和大海之间\r\n'.encode('utf-8'))
fobj2.close()

# 以追加写入
fobj3 = open('test3.txt', 'a')  # a:用于追加
fobj3.write('在乌云和大海之间\n')
fobj3.write('在乌云和大海之间\n')
fobj3.close()

# 以二进制格式打开，并追加写入
fobj4 = open('test4.txt', 'ab')  # a:用于追加
fobj4.write('在乌云和大海之间\n'.encode('utf-8'))
fobj4.write('在乌云和大海之间\n'.encode('utf-8'))
fobj4.close()

# 读的测试
# fobj5 = open('test.txt', 'a')  # a  用于追加数据
# fobj5.write('在苍茫的大海上')
# fobj5.write('狂风卷积着乌云')
# fobj5.write('在乌云和大海之间\n')
# fobj5.write('海燕像黑色的闪电\n')
# fobj5.write('今天我诗兴大发\n')
# fobj5.write('发感觉咋样呢\n')
# fobj5.close()

print('--------------------- r:形式读取')

f = open('Test5.txt', 'r')
print('----------读取所有的数据')
# print(f.read()) # 读取所有的数据

print('----------读取指定的数据量')
# print(f.read(12)) # 读取指定的数据量 不能和上面的 read() 同时读
# print(f.read()) # 上一次 读完的后，光标会在上一次读完的位置，下一次 继续读。

print('----------读取一行数据')
# print(f.readline())

print('----------读取所有数据, 返回一个列表，一行占一个数据项')
# print(f.readlines())
print(f.readlines(1)) # 只取第一行
f.close()  # 文件对象关闭


print()
print('--------------------- rb:形式读取')
f1 = open('Test5.txt', 'rb')
data = f1.read()
print(data)
print(data.decode('gbk')) # 读取所有的数据  使用 utf-8 会报错
f1.close() # 文件对象关闭



print()
print('--------------------- with的使用，上下文管理对象，优点：自动释放打开关联的对象')
with open('Test5.txt', 'r') as f:
    print(f.read())
    pass



'''
小结

文件读写的几种操作方式
read  r r+  rb  rb+
r r+ 只读  使用普通读取场景
rb  rb+  适用于 文件、图片、视频、音频 这样文件读取

write w  w+ wb+  wb a  ab
w wb+ w+  每次都会去创建文件
二进制读写的时候 要注意编码问题  默认情况下 我们写入文件的编码是gbk
a  ab a+  在原有的文件的基础之后去【文件指针的末尾】去追加，
并不会每次的都去创建一个新的文件

'''