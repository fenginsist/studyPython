# 类对象所拥有的方法，需要用装饰器 @classmethod 来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，类方法可以通过类对象，实例对象调用
# 类方法主要可以对类属性进行访问、修改

# 类对象所拥有的方法，需要用 @staticmethod 来表示静态方法


# 类方法、实例方法、静态方法对比
# 1. 类方法的第一个参数是类对象cls，通过cls引用的类对象的属性和方法
# 2. 实例方法的第一个参数是实例对象self，通过self引用的可能是类属性、也有可能是实例属性(这个需要具体分析)，`不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。`
# 3. 静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。


class People:
    country = 'china'

    # 类方法 用 classmethod 来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country  # 访问类属性
        pass

    @classmethod
    def change_country(cls, data):
        cls.country = data  # 修改类属性的值  在类方法中
        pass

    @staticmethod
    def getData():
        return People.country  # 通过类对象去引用
        pass

    @staticmethod
    def add(x, y):
        return x + y
        pass


print('-------------------类方法------------------------')
# print(People.get_country()) #通过类对象去引用
p = People()
print('实例对象访问 %s' % p.get_country())

print('-------修改之后')
People.change_country('英国')
print(People.get_country())  # 通过类对象去引用

print('-------------------静态方法------------------------')
print(People.getData())  # 类 访问 静态方法
a = People()
print(a.getData())  # 注意 一般情况下 我们不会通过实例对象去访问静态方法

print('-------带参数的静态方法')
print(People.add(10, 56))  # 带有参数的静态方法

'''
为什么要使用静态方法呢
由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互，
也就是说，在静态方法中， 不会涉及到类中方法和属性的操作
数据资源能够得到有效的充分利用
'''

# 案例：  返回当前的系统时间
print('-------------------案例：  返回当前的系统时间------------------------')
import time  # 引入第三方的时间模块


class TimeTest:
    def __init__(self, hour, min, second):
        self.hour = hour
        self.min = min
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())
        pass

    pass


print(TimeTest.showTime())
t = TimeTest(2, 10, 15)  # 这里的传参 没用，所以 使用类对象 去调用静态方法 ，多此一举
print(t.showTime())  # 没有必要通过这种方式去访问 静态方法
