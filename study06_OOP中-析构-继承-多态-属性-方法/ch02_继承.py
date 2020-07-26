# 在python中展现面向对象的三大特征:
# 封装、继承、多态
# 封装:指的是把内容封装到某个地方，便于后面的使用
# 继承: 和现实生活当中的继承是一样的：也就是 子可以继承父的内容【属性和行为】（爸爸有的儿子都有，相反 儿子有的爸爸不一定有）
#      所以对于面向对象的继承来说  其实就是将多个类共有的方法提取到父类中 子类仅需继承父类而不必一一去实现
#      这样就可以极大的提高效率 减少代码的重复编写，精简代码的层级结构 便于拓展
# 多态：顾名思义就是多种状态、形态，就是同一种行为 对于不同的子类【对象】有不同的行为表现

class Animal:
    def eat(self):
        '''
        吃
        :return:
        '''
        print('吃饭了')
        pass

    def drink(self):
        '''
        喝
        :return:
        '''
        pass


# 继承了Animal 父类 此时dog就是子类
class Dog(Animal):
    def wwj(self):
        '''
        子类独有的实现
        :return:
        '''
        print('小狗汪汪叫')

    pass


class Cat(Animal):
    def mmj(self):
        '''
        子类独有的实现
        :return:
        '''
        print('小猫喵喵叫')

    pass

print('**************dog 的行为**********************')
dog = Dog()
dog.eat()  # 具备了吃的行为  是继承了父类的行为
dog.wwj()

print('**************cat 的行为**********************')
cat = Cat()
cat.eat()
cat.mmj()
