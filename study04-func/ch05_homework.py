# 作业一、写函数，接收n个数字，求这些参数数字的和
def sumFunc(*args):
    result = 0
    for item in args:
        result += item
        pass
    return result
    pass


result1 = sumFunc(1, 2, 3, 46, 78, )
print('sumFunc(*args) 返回值：{}'.format(result1))


# 作业二、写函数，找出传入的 列表或元组 的  奇数位对应的元素  ，并返回一个新的列表
def processFunc(con):
    listResult = []
    index = 1

    for item in con:
        if index % 2 == 1:  # 判断奇数位
            listResult.append(item)
        pass
        index += 1
        pass
    return listResult
    pass


result2 = processFunc([1, 2, 3, 4, 5, 6, 70])
print('processFunc(con) 返回值：{}'.format(result2))


# 作业三、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# PS:字典中的value只能是字符串或列表
def dictFunc(dicParameter):  # **kwargs  这里可以用 关键字可变参数代替
    '''
    检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    :param dictParameter:
    :return:
    '''
    result = {}  # 空字典
    for key, value in dicParameter.items():
        if len(value) > 2:
            result[key] = value[:2]  # 向字典中添加数据
            pass
        else:
            result[key] = value
            pass
        pass
    return result
    pass


# 函数调用
dictPatam = {'name': '夏雨', 'hobby': ['唱歌', '跳舞', '运动', '编程'], 'pro': '中国艺术'}
dictResult = dictFunc(dictPatam)
print('dictFunc(dictParameter) 返回值：{}'.format(dictResult))
