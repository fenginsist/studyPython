# 函数返回值
'''
概念：函数执行完以后会返回一个对象，如果在函数的内部有return 就可以返回实际的值,否则返回None
类型：可以返回任意类型，返回值类型应该取决于return后面的类型
用途：给调用方返回数据
在一个函数体内可以出现多个return值：但是肯定只能返回一个return
如果在一个函数体内 执行了return,意味着函数就执行完成退出了，return后面的代码语句将不会执行
'''


def Sum(a, b):
    sum = a + b
    return sum  # 将计算的结果返回
    pass


rs = Sum(10, 30)  # 将返回值赋给其他的变量
print('10+30=%d' % rs)  # 函数的返回值返回到调用的地方

print('---------------测试返回的是 列表-----------------')
# 计算 1+2+。。。+num 的总数
def calComputer(num):
    '''
    计算 1+2+。。。+num 的总数
    :param num:
    :return: 返回 list列表
    '''
    li = []
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        pass
    li.append(result)
    return li
    pass


# 调用函数
value = calComputer(10)
print(type(value))  # value 的类型：list  <class 'list'>
print(value)

print('---------------测试返回的是 元组类型-----------------')
# 返回元组类型的数据
def returnTuple():
    '''
    :return: 返回元组类型的数据
    '''
    return 1,2,3
    pass


A = returnTuple()
print(type(A))

print('---------------测试返回的是 字典类型-----------------')
# 返回字典类型的数据
def returnDict():
    '''
    :return: 返回字典类型的数据
    '''
    return {"name": "测试"}
    pass


B = returnDict()
print(type(B))
