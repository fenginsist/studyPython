
# 自定义的异常类 ： ToolongMyException
class ToolongMyException(Exception):
    def __init__(self, leng):
        '''

        :param leng: 长度
        '''
        self.len = leng
        pass

    def __str__(self):
        return '您输入姓名数据长度是' + str(self.len) + '，超过长度了..'

    pass


def name_Test():
    name = input('请输入姓名.....')
    try:
        if len(name) > 5:
            raise ToolongMyException(len(name))             # 抛出异常
        else:
            print(name)
            pass
        pass
    except ToolongMyException as result:
        print(result)
        pass
    finally:
        print('执行完毕了....')


name_Test()
