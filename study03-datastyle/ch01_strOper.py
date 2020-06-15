# 字符串操作
test = 'python'

# 字符串测试
print('test 变量的类型：', type(test))
print('第一个字符:', test[0])
print('第一个字符:', test[1])

for item in test:
    print(item, end=' ')
    pass
print()

# 使用字符串方法
print('------------------1、capitalize()首字母转换大写-----------------------')
name = 'peter'
print('首字母转换大写 %s' % name.capitalize())

print('------------------2、strip()去掉两边的空格-----------------------')
a = '    hel lo    '
print('去掉两边的空格: %s' % (a.strip()))

print('------------------3、lstrip()去掉左边的空格-----------------------')
b = '    hel lo    '
print('去掉左边的空格: %s' % (b.lstrip()))

print('------------------4、rstrip()去掉右边的空格-----------------------')
c = '    hel lo    '
print('去掉右边的空格: %s' % (c.rstrip()))

print('------------------5、a 复制到 d-----------------------')
d = a
print('a 复制到 d: %s' % (d))

print('------------------6、id(a)查看内存地址-----------------------')
print('a 的内存地址:%d' % id(a))  # id（a）  id()函数，是查看地址的
print('d 的内存地址:%d' % id(d))

print('------------------7、find()查找子字符串是否存在-----------------------')
dataStr = 'I Love Python'
print('find()查找子字符串是否存在：%d' % (dataStr.find('Py')))  # find() 函数返回的是该字符串在整体字符串的第一个下标,找不到返回 -1

print('------------------8、index()查找子字符串是否存在-----------------------')
print('index()查找子字符串是否存在：%d' % (dataStr.index('o')))  # index() 函数 检测字符串中是否包含子字符串，返回的是下标值，找不到返回报错

print('------------------9、startswith()、endswith()判断字符串是否以某个字符串为开头或者结尾-----------------------')
print('判断字符串是否以某个字符串为开头：%s' % dataStr.startswith('I'))
print('判断字符串是否以某个字符串为结尾：%s' % dataStr.endswith('on'))

print('------------------11、将字符串转化为小写或者大写-----------------------')
print('将字符串转化为小写：%s' % dataStr.lower())
print('将字符串转化为大写：%s' % dataStr.upper())

print('------------------12、切片方法 slice [start: end:step]-----------------------')
strMsg = 'hello world'
# slice [start: end:step] 左闭右开， start<=value<end 范围
print('完整数据：%s' % strMsg)
print('字符串第一个字符：%s' % strMsg[0])
print(strMsg[2:5])  # 2-5下标之间的数据
print(strMsg[2:])  # 第三个字符到最后
print(strMsg[0:3])  # 1-3 strMsg[0:3]=strMsg[:3]
print(strMsg[:3])  # 1-3
print(strMsg[::-1]) # 倒叙输出 负号表示方向 从右边往左去遍历
