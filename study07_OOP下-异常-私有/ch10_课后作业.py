# *********************************************  有几个重点，认真看  *********************************************


# 1、Python中new方法作用是什么？
# 用来创建实例对象的，只有继承了object的话 才能有这个方法

# 2、什么是单例模式？单例模式适用于什么场景？
# 回答:
#  要求一个类有且只有一个实例，并且提供了一个全局的访问点
#  场景:日志插入logger的操作，网站计数器，权限验证模块，window资源管理器、系统回收站，数据库连接池

# 3、*********************私有化方法与私有化属性在子类中能否继承？ python 中什么不能被继承？？？？？？？？？？？？？？
# 不能的，私有属性和私有方法不可被继承

# 4、在Python中什么是异常？
#  异常就是程序在执行的过程中发生的错误

# 5、Python中是如何处理异常的。
#  分别根据  异常的类型  去处理

# 6、Python中异常处理语句的一般格式，可以使用伪代码的形式描述。
# try:
#     # 正常操作
# except：
#     # ......
# else:
#     # .....
# finally:
#     # .....

# 7、__slots__属性的作用
# 限制属性的随意输入
# 节省内存空间  __dict__

# 8、私有化属性的作用？
# 保护数据，封装性的体现

# 9、在类外面是否能修改私有属性。
# 不可以直接修改的 通过方法去实现  还可以借助属性函数 property去实现

# 10、如果一个类中，只有指定的属性或者方法能被外部修改。那么该如何限制外部修改。
#  对属性进行私有化的设定

# 1、编写一段代码以完成下面的要求
# 定义一个Person类,类中要有初始化方法,方法中要有人的姓名,年龄两个私有属性.
# 提供获取用户信息的函数.
# 提供获取私有属性的方法.
# 提供可以设置私有属性的方法.
# 设置年龄的范围在(0-120)的方法，如果不在这个范围，不能设置成功.

class Person:
    def __init__(self):
        self.__name = 'feng'
        self.__age = 10
        pass

    def __str__(self):
        return '{} 的年龄是{}'.format(self.__name, self.__age)
        pass

    # 第一种方式
    @property
    def name(self):
        return self.__name()
        pass

    @name.setter
    def name(self, name):
        self.__name = name
        pass

    # 第二种方式
    def get_age(self):
        return self.__age
        pass

    def set_age(self, age):
        if age < 0 and age > 120:
            print('年龄应该大于 0，小于 120 ')
        else:
            self.__age = age
        pass

    age = property(get_age, set_age)
    pass


print('操作题 1 :')
feng = Person()
print(feng)
feng.name = 'fanli'
feng.age = 25
print(feng)


# 2、*****************************请写一个单例模式
# 省略

# 3、创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。利用property 属性给调用者提供属性方式的调用获取和设置私有属性方法的方式。
class Student:
    def __init__(self):
        self.__name = '张三'
        self.__score = 90
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        pass

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
        pass

    def __str__(self):
        return self.__name

    # 这个 魔术方法 ，是 调用 实例对象(), 而触发的函数
    def __call__(self, *args, **kwargs):
        # print(self.__name+'的得分是:'+(str)self.__score)
        print('{}的得分是:{}'.format(self.__name, self.__score))
        pass

    pass

print('\n操作题 3:')
xw=Student()
xw() #将实例对象以函数的形式去调用
xw.name='李四'
xw.score=98
xw()
print(xw)

# 4、创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法,给类绑定一个类属性colour,给类绑定一个类方法打印字符串'ok'。
import types


def run(self):
    print('小猫飞快的跑...')
    pass


@classmethod
def info(cls):
    print('ok')


class Animal:
    pass

print('\n操作题 4:')

Animal.colour = '黑色'  # 绑定类属性
Animal.info = info
cat = Animal()
cat.run = types.MethodType(run, cat)  # 动态绑定
cat.run()
print(cat.colour)
Animal.info()
