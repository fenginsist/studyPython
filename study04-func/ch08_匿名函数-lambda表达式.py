# 匿名函数
# 语法
# lambda  参数1、参数2、参数3：表达式
# 特点
# 1、使用lambda关键字去创建函数
# 2、没有名字的函数
# 3、匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
# 4、匿名函数自带return ，而这个return 的结果 就是表达式计算后的结果

# 缺点
# lambda 只能是单个表达式，不是一个代码块，lambda 的设计就是为了满足简单函数的场景，
# 仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def来处理


print('-----------1、普通函数--------------')


# 1、正常的函数
def computer(x, y):
    '''
    计算数据和
    :param x:
    :param y:
    :return:
    '''
    return x + y
    pass


print(computer(10, 45))

print('-----------2、普通函数对应的匿名函数--------------')
# 2、对应的匿名函数
M = lambda x, y: x + y

# 通过变量去调用匿名函数
print(M(10, 45))

print('-----------3、第二个匿名函数--------------')
# 3、第二个匿名函数
result = lambda a, b, c: a * b * c
print(result(12, 34, 2))

# 4、类似于java的三元运算，
age = 15
print('-----------4、类似于java的三元运算--------------')
print('可以参军' if age > 18 else '继续上学')  # 可以替代传统多分支写法

print('-----------5、匿名函数+三元运算，求最大值--------------')
funcTest = lambda x, y: x if x > y else y
print(funcTest(2, 12))

print('-----------6、匿名函数 直接调用，随意--------------')
rs = (lambda x, y: x if x > y else y)(16, 12)
print(rs)

print('-----------7、匿名函数 + ** 幂运算--------------')
varRs = lambda x: (x ** 2) + 890
print(varRs(10))
