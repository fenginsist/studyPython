# __init__ 方法

print('----------------------引出问题，----------------------------')
class People:
    def eat(self):
        '''
        吃的行为
        :return:
        '''
        print('喜欢吃榴莲')
        pass

    pass


# 实例一
feng = People()
feng.name = '小倩'  # 可以通过对象添加属性，以下三个属性 都为 实例属性
feng.sex = '男'
feng.age = 20
feng.eat()
print(feng.name, feng.sex, feng.age)

# 实例二
fan = People()
fan.name = '小丽'
fan.sex = '女'
fan.age = 29
print(fan.name, fan.sex, fan.age)


# 以上创建对象时发现，如果有n个这个对象  被实例化  那么就需要添加很多次这样的属性了 显然是比较麻烦
# 因此 可以 使用 __init__ 方法  来创建创建
# 凡是 由 __ 开头 __结尾的 内置函数 称为 魔术方法
# __init__ 初始化方法，实例化对象的时候自动调用，完成一些初始化设置。

print('----------------------针对问题，使用魔术方法、python内置方法 __init__方法 添加属性----------------------------')
class People1:

    def __init__(self):  # 初始化方法，实例化对象的时候自动调用，完成一些初始化设置。
        '''
        实例属性的声明
        '''
        self.name = '小冯'
        self.sex = '男'
        self.age = 20
    pass

    def eat(self):
        '''
        吃的行为
        :return:
        '''
        print('喜欢吃榴莲')
    pass
pass


# 实例三  新建的实例已经具备的 类中初始的值
li = People1()
li.name = '老大'
print(li.name, li.sex, li.age)


print('----------------------再次改进People 类，对其传参数，类似于java的 构造函数----------------------------')
# 改进 People 类
class People2:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    pass

    def eat(self,food):
        '''
        吃的行为
        :return:
        '''
        print(self.name+'喜欢吃'+food)
    pass
pass

# 实例四
xiao = People2('冯凡利','man',18)
print(xiao.name, xiao.sex, xiao.age)
xiao.eat('香蕉')


# 总结 __init__ 方法
# 1. python 自带的内置函数 具有特殊的函数   使用双下划线 包起来的【魔术方法】
# 2. 是一个初始化的方法 用来定义实例属性 和初始化数据的，在创建对象的时候自动调用  不用手动去调用
# 3. 利用传参的机制可以让我们定义功能更加强大并且方便的 类


