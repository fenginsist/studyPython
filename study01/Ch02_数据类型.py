'''
python的基本数据类型
1、数字 num :包括五个
    a、 int(有符号整数)
    b、 long（长整形）（python 3 取消，都用int 代替）
    c、 float(浮点型)
    d、 complex(复数)
    e、 布尔值（bool）： True False
2、字符串 str
3、字典 dict
4、元组 tuple
5、列表 list
'''

# 数字 int
a = 10
print(type(a))

# 数字 float
a = 12.67
print(type(a))

# 数字 complex
a = 2.4 + 5j
print(type(a))

# 数字 bool
a = True
print(type(a))

# 字符串
a = '冯凡利'
print(type(a))

print('--------高级类型----------')

# 字典类型 dict
b = {}
print(type(b))

# 元组类型 tuple
b = ()
print(type(b))

# 列表类型 list
b = []
print(type(b))
