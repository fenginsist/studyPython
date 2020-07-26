# 1、求三组连续自然数的和：求出1到10、20到30和35到45的三个和

def sumRange(m, n):
    '''
    求 从 m 到 n 的连续自然数的总和
    :param m: 开始值
    :param n: 结束值
    :return:
    '''
    return sum(range(m, n + 1))
    pass


print(sumRange(1, 10))
print(sumRange(20, 30))
print(sumRange(35, 45))


# 2、100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头。请问大小和尚各多少人？
def personCount():
    '''
    计算各有多少个和尚
    假设 大和尚 a 小和尚 100-a
    :return:
    '''
    for a in range(1, 100):
        if a * 3 + (100 - a) * (1 / 3) == 100:
            # 100 个和尚 吃 100个 馒头
            return (a, 100 - a)
            pass
        pass

    pass


res = personCount()
print('大和尚{}人，小和尚{}人'.format(res[0], res[1]))

# 3、指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个“独一无二”的数字
li = [1, 3, 4, 3, 3, 5, 7, 2, 4, 2, 5, 2, 1]
print('指定的列表：{}'.format(li))
set1 = set(li)
print('set1:{}'.format(set1))  # 去重后的数据 set1:{1, 2, 3, 4, 5, 7}

for i in set1:
    li.remove(i)
    pass
print('清除后的 列表：{}'.format(li))

set2 = set(li)  # set2中为原来li中有重复的数字集合

for i in set1:  # set1中数据全部去重后形成的集合
    if i not in set2:
        print(i)
        pass
    pass
pass

if 1 not in (1, 2):
    print(1)
    pass
else:
    print(2)