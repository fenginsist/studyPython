# 1、python中如何通过类创建对象，请用代码举例说明。
class Student:
    def run(self):
        print('学生每天进行2000米的跑步训练')
        pass

    pass

print('----------- 作业一 ------------')
xiaoli = Student()  # 创建一个对象
xiaoli.run()


# 2、如何在类中定义一个方法，请用代码举例说明。
# 参考上述demo

# 3、定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象 并 分别添加上颜色属性
class SgClass:
    def __init__(self, name, color):
        '''
        :param name:
        :param color:
        '''
        self.color = color
        self.name = name
        pass

    def __str__(self):
        return '%s 的颜色是【%s】' % (self.name, self.color)

    pass

print('----------- 作业三 ------------')
pg = SgClass('苹果', '红色')
pg.zj = 10  # 通过对象添加对象属性
print(pg)
jz = SgClass('橘子', '橙色')
print(jz)
xg = SgClass('西瓜', '黑皮')
print(xg)


# 4、请编写代码，验证 self 就是实例本身。
class Person:
    def weight(self):
        print('self=%s' % id(self))

    pass

print('----------- 作业四 ------------')
liming=Person()
liming.weight()
print(id(liming))

# 5、定义一个Animal类
# (1)、使用__init__初始化方法为对象添加初始属性。如颜色，名字，年龄。
# (2)、定义动物方法，如run，eat等方法。如调用eat方法时打印xx在吃东西就可以。
# (3)、定义一个__str__方法，输出对象的所有属性。

class Animal:
    def __init__(self, color, name, age):
        '''

        :param color:
        :param name:
        :param age:
        '''
        self.color = color
        self.name = name
        self.age = age
        pass

    def eat(self):
        print('%s 在吃东西' % self.name)
        pass

    def run(self):
        print('%s 在飞快的跑' % self.name)
        pass

    def __str__(self):
        return '%s 的颜色是:%s 今年 %d 岁了' % (self.name, self.color, self.age)

    def __del__(self):
        print('xhl')

    pass

print('----------- 作业五 ------------')
tigger = Animal('黄色', '东北虎', 4)
tigger.run()
tigger.eat()
print(tigger)
# del tigger
input('ddz')
