class God:
    def fly(self):
        print("神仙都会飞")

    pass


class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')

    pass


class Sunwukong(God, Monkey):  # 即使神仙  同时也是猴子
    pass


swk = Sunwukong()
swk.chitao()
swk.fly()

print('--------------------------多继承存在的问题：当继承的类中，有共同的方法时，执行哪一个')

# 存在的问题
# 问题是  当多个父类当中存在相同方法的时候  应该去调用哪一个呢
class D(object):
    def eat(self):
        print('D.eat')
        pass

    pass


class C(D):
    def eat(self):
        print('C.eat')
        pass

    pass


class B(D):
    pass


class A(B, C):
    pass


a = A()
a.eat()  # C.eat
print(A.__mro__)
# A.__mro__  可以显示类的依次继承关系
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
# 先找到 A，在找B，如果B中没有，就找C，如果C中没有，则找B继承的D中，如果没找到，再找C继承到的D中，如果还没有，在找D继承的 Object类


# 在执行eat的方法时 查找方法的顺序是
# 首先到A里面去查找  如果A中没有 则继续的去B类中去查找 如果B中没有
# 则去C中查找 如果C类中没有 则去D类中去查找，如果还是没有找到 就会报错
# A-B-C-D  也是继承的顺序
