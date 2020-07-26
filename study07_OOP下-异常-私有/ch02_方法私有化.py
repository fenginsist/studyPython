# 概述：
# 私有化方法跟私有化属性概念一样，有些重要的方法，不允许外部调用，防止子类意外重写，把普通的方法设置成私有化方法。

# 语法：
# 私有化方法，即在方法名前面加两个下划线。

# 示例:
# class A(object):
#     def __myname(self):
#         pass
#     pass

# 总结：
# 私有化方法一般是类内部调用，子类不能继承，外部不能调用。

# 单下划线、双下划线、头双下划线、头尾双下划线说明
# _xxx 前面加一个下划线，以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能使用from xxx import * 的方式导入。
# __xxx__ 前后两个下滑线，魔法方法，一般是python自有，开发者不要创建这类型的方法。
# __xxx 前面两个下划线，私有属性或者私有方法的定义。
# xxx_ 后面单下滑线，避免属性名与python关键字冲突

class Animal:

    # 私有方法 的定义
    def __eat(self):
        print('吃东西')
        pass

    def run(self):
        self.__eat()  # 在此调用私有化的方法
        print('飞快的跑')

    pass


class Bird(Animal):
    pass


b1 = Bird()
# print(b1.eat())
# b1.eat()  # 报错，实例对象 不能调用私有方法
b1.run()
