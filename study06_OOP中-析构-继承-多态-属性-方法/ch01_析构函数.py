# 析构函数

# 最后析构方法总结
# 1、当整个程序脚本执行完毕后会自动调用__del__方法
# 2、当对像被手动销毁时也会自动调用 __del__ 方法
# 3、析构函数一般用于资源回收，利用__del__方法销毁对象回收内存等资源


class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造初始化方法')
        pass

    def __del__(self):
        # 主要的应用就是来操作 对象的释放  一旦释放完毕  对象便不能在使用
        print('当在某个作用域下面 没有被使用【引用】的情况下 解析器会自动的调用此函数 来释放内存空间')
        print('这是析构方法')
        print('%s 这个对象 被彻底清理了 内存空间也释放了' % self.name)

    pass


print('---cat 实例')
cat = Animal('小花猫')

# del cat  #手动的去清理删除对象  会指定__del__函数

print(cat.name)
input('程序等待中.....')  # 有这一句话时，会暂停

print('--- dog 实例')
dog = Animal('柯基小狗')
