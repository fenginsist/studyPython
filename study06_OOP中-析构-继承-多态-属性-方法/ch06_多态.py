# 案例演示
class Animal:
    '''
    父类【基类】
    '''

    def say_who(self):
        print('我是一个动物....')
        pass

    pass


class Duck(Animal):
    '''
      鸭子类 【子类】 派生类
    '''

    def say_who(self):
        '''
        在这里重写父类的方法
        :return:
        '''
        # super().say_who()
        print('我是一只漂亮的鸭子')
        pass

    pass


print('--------------鸭子类继承动物类')
duck1 = Duck()
duck1.say_who()


class Dog(Animal):
    '''
     小狗类 【子类】 派生类
    '''

    def say_who(self):
        print('我是一只哈巴狗')
        pass

    pass


print('--------------狗类继承动物类')
dog1 = Dog()
dog1.say_who()


class Cat(Animal):
    '''
        小猫类 【子类】 派生类
    '''

    def say_who(self):
        super().say_who()
        print('我是一只小花猫 喵喵喵喵')
        pass

    pass


print('--------------猫类继承动物类')
cat1 = Cat()
cat1.say_who()


class Bird(Animal):
    '''
    新增鸟类 无需修改原来的代码
    '''

    def say_who(self):
        print('我是一只黄鹂鸟')

    pass


class People:
    def say_who(self):
        print('我是人类')

    pass


class student(People):
    def say_who(self):
        print('我是一年级的学习 张明')

    pass


def commonInvoke(obj):
    '''
    统一调用的方法
    :param obj: 对象的实例
    :return:
    '''
    obj.say_who()


print('--------------案例：for循环+列表')

listObj = [Duck(), Dog(), Cat(), Bird(), student()]

for item in listObj:
    '''
     循环去调用函数
    '''
    commonInvoke(item)
