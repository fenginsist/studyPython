# 模块的制作说明

'''
__name__ :魔术变量  在本文件中  值为 __main__ ,在外面调用为 文件名
__all__: 魔术变量， 作用：指定外面可以调用的方法 如果在一个文件中存在 __all__ 遍历，那么意味着这个变量中的元素会被
            from XXX import 导入， 对于import 方式来讲 无所谓有没有，都可以全部的引用。

'''

__all__ = ['add', 'diff']


def add(x, y):
    '''
    普通的函数
    :param x:
    :param y:
    :return:
    '''
    return x + y
    pass


def diff(x, y):
    return x - y


def printInfo():
    print('这是自定义的方法')
    pass


if __name__ == '__main__':
    res = add(1, 3)
    print('测试res', res)
    print('模块的魔术遍历__name__:%s' % __name__)
    pass
