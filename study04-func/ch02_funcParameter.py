'''
参数的分类：
必须参数、默认参数[缺省参数]、可选参数、关键字参数
参数：其实就是函数为了实现某项特定的功能，今儿为了得到实现功能所需要的数据
为了得到外部数据
'''


# 1、必选参数
def sum(a, b):  # 形式参数：形参，知识意义上的一种参数，在定义的时候是不占用内存地址的
    sum = a + b
    print(sum)
    pass


# 2、默认参数【缺省参数】  始终存在于参数列表中的尾部
def sum1(a, b=30):
    print('默认参数使用=%d' % (a + b))
    pass


# 3、可变参数(当参数的个数不确定时使用，比较灵活
# 可变参数 为元组类型
def getComputer(*args):  # 可变长的参数
    '''
    计算累加和
    :param args:  可变长的参数类型, 为元组
    :return:
    '''
    result = 0
    for item in args:
        result += item
        pass
    print('可变参数类型：', type(args))
    print('result=%d' % result)
    pass


# 4、关键字可变参数  0-n
# ** 来定义
# 在函数体内 参数关键字是一个 字典类型 key是一个字符串
def keyFunc(**kwargs):
    # 参数关键字是一个 字典类型
    print(kwargs)
    pass


# 可变参数（*args）和 关键字可变参数（**kwargs）  # 可选参数 必须放到 关键字可选参数  之前
def complexFunc(*args, **kwargs):
    '''
    可选参数 必须放到 关键字可选参数  之前
    可选参数：接受的数据是一个元组类型
    关键字可选参数：接受的数据是一个字段类型
    :param args:
    :param kwargs:
    :return:
    '''
    print(args)
    print(kwargs)
    pass


# 函数调用    在调用的时候必选参数 是必须要赋值的
print('-----1、调用 必选参数 函数------')
sum(20, 15)  # 20， 15 实际参数： 实参，实实在在的参数，是四级占用内存地址的

print('-----2、调用 默认参数【缺省参数】 函数------')
sum1(20)  # 在调用的时候 如果未赋值，就会用定义函数时给定的默认值

print('-----3、调用 可变参数（*args） 函数------')
getComputer(1)  # 传入一个数 为元组
getComputer(1, 2)

print('-----4、调用 关键字可变参数（**kwargs） 函数------')
# keyFunc(1, 2, 3)  # 不可以传递的
dictA = {'name': 'feng', 'age': 23}
# keyFunc(dictA)  # TypeError: keyFunc() takes 0 positional arguments but 1 was given
keyFunc(**dictA)
keyFunc(name='feng', age=23)
keyFunc()

print('-----4、调用 可变参数（*args）和关键字可变参数（**kwargs） 函数------')
complexFunc()
complexFunc(1, 2, 3, 4, 5)
complexFunc(1, 2, 3, 4, 5, name='刘德华')
