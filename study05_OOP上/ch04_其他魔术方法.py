# 学习其他常用魔术方法

# __init__(self) 初始化一个类，在创建实例对象为其赋值时使用。
# __str__(self) 在将对象转换成字符串  str(对象)  测试的时候，打印对象的信息。
# __new__(cls, *args, **kwargs) 创建并返回一个实例对象，调用了一次，就会得到一个对象。
# __class__ 获得已知对象的类 ( 对象.__class__)。
# __del__方法：对象在程序运行结束后进行对象销毁的时候调用这个方法，来释放资源。

# 执行的顺序：
# 1、__new__ 先创建实例 2、__init__ 初始化类    总结：实例化，再初始化类


print('---------------案例一：不使用__str__()')


class Person:
    def eat(self):
        print('吃东西')
        pass

    pass


dog = Person()
print(dog)

print('---------------案例二：使用__str__()：打印对象 自定义对象 是内容格式的')


class Person1:

    def __init__(self, pro, name, food):
        '''
        初始化方法
        :param pro: 专业
        :param name: 姓名
        :param food: 食物
        '''
        self.pro = pro  # 实例属性的定义
        self.name = name
        self.food = food
        print('----init-----函数执行')
        pass

    def __str__(self):
        '''
        打印对象 自定义对象 是内容格式的
        :return:
        '''
        return '%s 喜欢吃 %s 修的专业是:%s' % (self.name, self.food, self.pro)
        pass

    pass


cat = Person1('计算机', '冯凡利', '鸡蛋')
print(cat)

print('---------------案例三：使用__new__(cls, *args, **kwargs):创建对象实例的方法 -------------------')


class Person2:

    def __init__(self, pro, name, food):
        '''
        初始化方法
        :param pro: 专业
        :param name: 姓名
        :param food: 食物
        '''
        self.pro = pro  # 实例属性的定义
        self.name = name
        self.food = food
        print('----init-----函数执行')
        pass

    def __str__(self):
        '''
        打印对象 自定义对象 是内容格式的
        :return:
        '''
        return '%s 喜欢吃 %s 修的专业是:%s' % (self.name, self.food, self.pro)
        pass

    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法  每调用一次 就会生成一个新的对象 cls 就是 class 的缩写

        场景：可以控制创建对象的一些属性限定 经常用来做单例模式的时候来使用
        :param args:
        :param kwargs:
        '''
        print('----new-----函数的执行')
        return object.__new__(cls)  # 在这里是真正创建对象实例的
        pass

    pass


cat = Person2('计算机', '冯凡利', '鸡蛋')
print(cat)
# 如果在 __new__方法中，注释掉  return object.__new__(cls) 这句话， print(cat) 打印出 None
