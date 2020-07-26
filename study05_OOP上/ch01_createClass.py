# 定义类和对象
# 类的三要素：类名、属性、方法

# 类结构  类名  属性  方法
# class 类名:
#     属性
#     方法

# 一、方法
# 1. 普通方法，类外面
# 2. 实例方法 归实例（对象）所有，在类的内部，使用 def 关键字可以定义一个实例方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

# 二、属性
# 类里面定义的变量。
# 1. 定义在类里面，方法外面的属性称之为  类属性，
# 2. 定义在方法里面使用self引用的属性称之为  实例属性


class Person:
    '''
    对应人的特征
    '''
    # name='小明'  #类属性
    age = 20  # 类属性

    '''
    对应人的行为  实例方法:第一个参数 为 self 或者为 其他名称
    '''

    def __init__(self):
        self.name = '小明'  # 实例属性   # 可以通过self.name  来创建 实例属性
        pass


    def eat(parms):
        print("大口的吃饭")
        pass

    def run(self):  # 实例方法
        print('飞快的跑')
        pass

    pass


# 普通方法
def printInfo():
    '''
    普通方法
    :return:
    '''
    pass


# 创建一个对象【类的实例化】
# 规则格式  对象名=类名()
xm = Person()
xm.eat()  # 调用函数
xm.run()

print("{}的年龄是：{}".format(xm.name, xm.age))

# 创建另外一个实例对象
xw = Person()
xw.eat()  # 实例方法
