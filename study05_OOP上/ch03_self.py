# self 的学习

# 从前面中知道，这个 self 仅在创建实例方法时创建，创建普通方法时不需要，self 可以更改的，只是我们约定俗成的 用self。
# 这里的 self 类似于 java 的 this指针，只不过 java 构造函数的形参不写 this， 而这里的实例方法 中的第一个参数为 self。相当于 显示出来这个引用对象

class Person:

    def __init__(self, pro):
        '''

        :param pro: 专业
        '''
        self.pro = pro # 实例属性的定义
        pass

    def eat(self):
        '''
        实例方法
        :return:
        '''

        print(self)
        pass

    def eat2(self):
        '''
        实例方法
        :return:
        '''
        print('self=%s', id(self))
        pass

    def eat3(a, name, food):
        '''
        实例方法
        :return:
        '''
        print('%s 喜欢 %s, 修的专业为 %s'%(name, food, a.pro))
        pass
    pass

print('------ 实例一：feng ------')
feng = Person('计算机')
feng.eat()  # <__main__.Person object at 0x000001F383935AC0>

# 发现  self 是一个对象，

print('------ 实例二：fan ------')
fan = Person('计算机')
print('fan=%s',id(fan)) # fan=%s 2344879106896
fan.eat2() # self=%s 2344879106896
fan.eat()  # <__main__.Person object at 0x00000221F5AFAB50>
print(fan)  # <__main__.Person object at 0x00000221F5AFAB50>

print('------ 实例三：li ------')
li = Person('吃饭')
li.eat3('小冯','蛋糕')

# self 和 对象 指向同一个内存地址，可以认为 self 就是对象的引用。  java 中类似于 this

# 小结  self特点
# self 只有在类中定义 实例方法的时候才有意义, 在调用时候不必传入相应的参数 而是由解释器 自动去指向
# self 的名字是可以更改的  可以定义成其他的名字，只是约定俗成的定义成了 self
# self 指的是 类实例对象本身, 相当于java中 this


# __new__和__init___函数的区别
# __new__ 类的实例化方法 必须要返回该实例 否则对象就创建不成功
# __init___ 用来做数据属性的初始化工作  也可以认为是实例的构造方法  接受类的实例 self 并对其进行构造
# __new__   至少有一个参数是 cls 代表要实例化的类 ，此参数在实例化时由python解释器自动提供
# __new__  函数 执行要早于 __init___ 函数
