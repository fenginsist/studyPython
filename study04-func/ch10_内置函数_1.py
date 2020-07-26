# python 的内置函数

# 运算函数
print('-------------------------运算函数---------------------------')

print('---------abs() 取绝对值')
# 取绝对值
print(abs(-34))

print('---------round() 取近似值')
# round  取近似值， 后面的 1 为保留几位数，输出 3.7， 如果没有后面的1 则输出 4，默认取整
print(round(3.66, 1))

print('---------pow() 求次方， 类似于 ** 算法')
# pow 求次方
print(3 ** 3)
print(pow(3, 3))

print('---------max() 求最大值')
# max 求最大值
print(max([23, 123, 4, 5, 2, 1, 786, 234]))
print(max(23, 235))

print('---------sum(可迭代对象，如：列表、 元组、集合, 参数) 求和,可使用 range（）函数迭代')
# sum 使用， 后面 参数，为range函数算完之后，再加上这个参数
print(sum(range(3, 4), 3))
print(sum([3], 3))

print('---------eval() 动态执行表达式（表达式为字符串）')
# eval 执行表达式
a, b, c = 1, 2, 3
print('动态执行的函数={}'.format(eval('a*b+c-30')))


def TestFun():
    print('我执行了吗?')
    pass


eval('TestFun')  # 不可以调用函数执行
eval('TestFun()')  # 可以调用函数执行

print('-------------------------类型转换函数---------------------------')
# 类型转换函数

print('---------类型转换 int()转为整型 ')
# int() 函数用于将一个字符串或数字转换为整型  语法: class int(x, base=10)  base -- 进制数，默认十进制
print(int('555'))
print(int(3.6))

print('---------类型转换 float() 转换成浮点数')
# float() 函数用于将整数和字符串转换成浮点数
print(float(3))
print(float('3.6'))

print('---------类型转换 str() 转化为字符串')
# str() 函数将对象转化为适于人阅读的形式
a = 1
print(type(a))
b = str(a)
print(type(b))

print('---------类型转换 ord()字符转数字')
# 描述: ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的
# 配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

print('---------类型转换 chr()数字转字符')
# 描述: chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
# 语法: chr(i)
# 参数: i -- 可以是10进制也可以是16进制的形式的数字
# 返回值:返回值是当前整数对应的ascii字符
print(chr(65))
print(chr(91))

print('---------类型转换 bool()转为布尔型  下列对象都相当于False：[],(),{},0, None, 0.0, ''')
# 描述: bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
# 语法: class bool([x])
# 参数: x -- 要进行转换的参数
# 返回值:返回 Ture 或 False
print(bool(0))
print(bool(()))
print(bool([]))
print(bool(12))

print('---------类型转换 bin() 十进制转二进制')
print(bin(10))  # 转换二进制   #  0b1010

print('---------类型转换 hex() 十进制转十六进制')
print(hex(23))  # 十六进制    #  0x17

print('---------类型转换 oct() 十进制转八进制')
print(oct(10))  # 八进制      #  0o12

print('---------类型转换 元组转换为列表')
# 元组转换为列表
tup = (1, 2, 3, 4)
print(type(tup))
li = list(tup)  # 强制转换
print(type(li))
li.append('强制转换成功')
print(li)

print('---------类型转换 列表转换为元组')
# 列表转换为元组
tupList = tuple(li)
print(type(tupList))

print('---------类型转换 字典操作 dict()')
# 字典操作 dict()
dic = dict()  # 创建一个字典
# dic = dict(name='小明', age=18)  # 创建一个字典
print(type(dic))
dic['name'] = '小明'
dic['age'] = 18
print(dic)

print('---------类型转换 bytes转换')
# bytes转换
print(bytes('我喜欢python', encoding='utf-8'))
