# 概述，通过前面的讲解，私有变量的访问，一般写两个方法一个访问，一个修改，由方法去控制访问。

# 例如:
class P(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    def get_age(self):  # 访问私有类属性
        return self.__age

    def set_age(self, age):  # 修改私有属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age

    pass


# 这样给调用者的感觉就是调用了一个方法，并不是访问属性。怎么做到让调用者直接以访问属性的方式，而且我们又能控制的方式提供给调用者？

# 实现方式 1
'''
Python中有一个被称为属性函数(property)的小概念
示例：给age属性设置值时，会自动调用setage方法，获取age属性值时，会自动调用getage方法。
在上面的例如中最下面添加一句：age = property(get_age,set_age)
定义一个属性，当对这个age设置值时调用set_age,当获取值时调用get_age
注意：必须是以get,set开头的方法名，才能被调用
'''
xiaoming = P()
xiaoming.age = 15
print(xiaoming.age)


# 实现方式 2
# 装饰器，即在方法上使用装饰器
class P1(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    @property  # 使用装饰器对age进行装饰，提供一个getter方法
    def age(self):  # 访问私有类属性
        return self.__age

    @age.setter  # 使用装饰器进行装饰，提供一个setter方法
    def age(self, age):  # 修改私有属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age

    pass


xiaoming = P1()
xiaoming.age = 15
print(xiaoming.age)


                                                    # 以下为案例


class Person(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加连个 __ 下滑线
        pass

    def get_age(self):  # 访问私有实例属性
        return self.__age
        pass

    def set_age(self, age):  # 修改私有实例属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
        pass

    # 定义一个类属性  实现通过直接访问属性的形式去访问私有的属性
    age = property(get_age, set_age)
    pass


print('------------------实现方式-1')
p1 = Person()

print(p1.age)  # 方式一、获取值

p1.set_age(12)  # 方式一、设置值
print(p1.get_age())  # 方式二、获取值

p1.age = 25  # 方式二、设置值
print(p1.get_age())


class Person1(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加连个 __ 下滑线
        pass

    # 使用装饰器对age进行装饰，提供一个getter方法
    @property
    def age(self):  # 访问私有实例属性
        return self.__age
        pass

    # 使用装饰器进行装饰，提供一个setter方法
    @age.setter
    def age(self, age):  # 修改私有实例属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
        pass

    pass


print('------------------实现方式-2')
p2 = Person1()
print(p2.age)

p2.age = 20

print(p2.age)
