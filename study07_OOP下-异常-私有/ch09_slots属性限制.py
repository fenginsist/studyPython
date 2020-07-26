# 前面 一节说到 可以动态添加属性（实例属性、类属性）和方法（类方法、静态方法）
# 所以便定义一个 __solts__ 属性，来限制该class实例能添加的属性。可以防止其他人在调用类的时候胡乱添加属性或方法。__slots__属性子类不会继承，只有在当前类中有效。
# __slots__属性子类不会继承，只有在当前类中有效。
# 语法 看下面实例

# __slots__ 的作用：
# 限制要添加的实例属性
# 节约内存空间


class Student(object):
    __slots__ = ('name', 'age', 'score')  # 指定 动态添加属性 的属性范围。

    def __str__(self):
        return '{}....{}'.format(self.name, self.age)

    pass


print('----------案例一：打印对象:xw和 __solts__-------------')
xw = Student()
xw.name = '小王'
xw.age = 20
print(xw)
xw.score = 96  # 没有在范围内 所以报错，在 __slots__中指定即可

# 所有可以用的属性都在这里存储  不足的地方就是占用的内存空间大，
# 要打印这个必须要注释 掉 __slots__ 属性，因为定义__slots__之后，所有的属性就不在__dict__中了
# 可以看到 在定义了 slots变量之后 student类的实例已经不能随意创建不在 __slots__定义的属性了
# 同时还可以看到实例当中也不在有__dict__
# print(xw.__dict__)  # {'name': '小王', 'age': 20, 'score': 96}


# 在继承关系当中的使用  __slots__
# 子类未声明  __slots__时，那么是不会继承父类的__slots__，此时子类是可以随意的属性赋值的
# 子类声明 了__slots__时，继承父类的__slots__，也就是子类__slots__的范围是为
# 其自身+父类的__slots__

print('----------案例二：继承带有__slots__属性的类 -------------')


class subStudent(Student):
    # __slots__ = ('gender', 'pro')
    pass


ln = subStudent()
ln.gender = '男'
ln.pro = '计算机信息管理'
ln.name = 'feng'
ln.age = 12
ln.score = 60
print(ln.gender, ln.pro)

print(ln)  # 使用了父类的 __str__() 方法
