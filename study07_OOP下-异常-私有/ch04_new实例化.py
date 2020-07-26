




class Animal:
    def __init__(self):
        self.color = 'red'
        print('init 执行了')
        pass

    # 在python当中, 如果不重写 __new__ 默认结构如下
    def __new__(cls, *args, **kwargs):
        print('new 执行了')
        return super().__new__(cls, *args, **kwargs)
        # return object.__new__(cls, *args, **kwargs)  # 这个也可以
        pass

    pass


tigger = Animal()  # 实例化的过程会自动调用__new__去创建实例

# 在新式类中 __new__  才是真正的实例化的方法，为类提供外壳制造出实例框架，然后调用该框架内的构造方法__init__ 进行丰满操作
# 比喻建房子 __new__   方法负责开发地皮 打地基 并将原料存放在工地，而__init__ 负责从工地取材料建造出地皮开发图纸规定的大楼，
# 负责细节设计、建造 最终完成
