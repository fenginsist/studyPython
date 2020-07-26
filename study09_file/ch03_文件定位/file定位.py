# tell  返回指针当前所在的位置
# 对于中文讲 每次读取到的一个汉字 实际上占用了 2个字符,, 每个英文 占用 1 个字符
print('---------------------tell() 方法：返回指针当前所在的位置')
# with open('Test5.txt', 'r+') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())
#     pass

# truncate 可以对源文件进行截取操作
print('---------------------truncate() 方法：可以对源文件进行截取操作')
fobjB = open('Test5.txt', 'r')
print(fobjB.read())
fobjB.close()

print('截取之后的数据........')
# fobjA = open('Test5.txt', 'r+')
# fobjA.truncate(15)  # 保留前15个字符
# print(fobjA.read())
# fobjA.close()
'''
我特意试了一下 截取 汉字 ，
会报错 ：UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf in position 14: incomplete multibyte sequence
'''

print('---------------------seek() 方法：可以控制光标所在位置,注意：一个汉字等于两个英文字母 占两个字节')
# seek 可以控制光标所在位置
with open('Test5.txt', 'rb') as f:
    f.seek(4, 0)  # 光标是从0的位置开始 像前【右】移动 4个字符
    data = f.read(2)
    print(data.decode('gbk'))
    f.seek(-2, 1)  # 相当于光标有设置到了0的位置
    print(f.read(4).decode('gbk'))
    f.seek(-6, 2)  # 2 表示光标在末尾处  往回移动了6个字符
    print(f.read(4).decode('gbk'))
    pass

# 对于这种情况 用'r'这种模式打开文件，在文本文件中，没有使用二进制的选项打开文件，
# 只允许从文件的开头计算相对位置，从文件尾部计算或者当前计算的话 就会引发异常
