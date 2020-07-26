# 定义了两个初始属性name和age，但是没有颜色，我想要添加颜色又不能去修改类
# 这时就可以动态绑定属性了
# 一、动态添加实例属性
# 实例对象.要添加的属性名=对应值。即可

# 二、动态添加类属性
# 类对象.要添加的属性名=对应值。即可

# 三、动态添加实例方法 ： 添加方法需要 types 方法，先导入 import types
# 实例对象.方法名 = types。MethodType（定义的方法名，实例对象） # 利用types方法绑定实例属性


# 四、动态绑定类方法（@classmethod）和静态方法（@staticmethod）
# 类对象.方法名 = 定义的方法名 （）


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return '{}今天{}岁了'.format(self.name, self.age)
        pass

    pass


print('-------------一、动态添加：实例属性---------------')
print('---实例 1: zyh')
zyh = Student('张艳华', 20)
zyh.weight = 50  # 动态添加
print(zyh)
print(zyh.weight)

print('---实例 2:zm')
zm = Student('张名', 20)
print(zm)
# print(zm.weight)  # 报错 'Student' object has no attribute 'weight'


print('-------------二、动态添加属性：类对象属性---------------')
Student.shcool = '北京邮电大学'  # 动态添加类属性
print(zm.shcool)

print('-------------三、动态添加方法：类对象属性，需要引入添加方法的库---------------')
import types  # 添加方法的库


def dymicMethod(self):
    print('{}的体重是:{}kg 在 {} 读大学'.format(self.name, self.weight, Student.shcool))
    pass


# 将下面的类方法和静态方法 动态添加到 Student类上
@classmethod
def classMethodTest(cls):
    print('这是一个类方法')
    pass


@staticmethod
def staticMethodTest(cls):
    print('这是一个静态方法')
    pass


print('-----zyh 实例:types.MethodType(方法名,实例)绑定方法')
zyh.printInfo = types.MethodType(dymicMethod, zyh)  # 动态的绑定方法
zyh.printInfo()
print('-----zm 实例:types.MethodType(方法名,实例)绑定方法')
zm.printInfo = types.MethodType(dymicMethod, zm)  # 给 zm 动态绑定方法
zm.weight = 20  # 给 zm 动态添加属性
print(zm.weight)
zm.printInfo()

print('-------------四、动态添加方法：绑定类方法---------------')
Student.classTest = classMethodTest
Student.classTest()

print('-------------五、动态添加方法：给类绑定静态方法---------------')
Student.staticTest = staticMethodTest
Student.staticTest()
