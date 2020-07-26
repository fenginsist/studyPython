# 序列函数操作 str 元组、 list
print('-------------------------序列函数操作 str 元组、 list---------------------------')

# all()  result:bool 对象中的元素除了是 0、空、FALSE 外都算 TRUE, 只要有这三个 就为false，。 似于逻辑运算符 and 的判断
# 结果就为True
print(all([]))  # True
print(all(()))  # True
print(all([1, 2, 4, False]))  # false
print(all([1, 2, 4]))  # True
print(all((3, 4, 0)))  # false

# any  result:bool 类似于逻辑运算符 or 的判断，只要有一个元素为 True 结果就为 True
print('--------any')
print(any(('', False, 0)))  # false
print(any((1, 2, 3)))  # True

print('-------- sort 和 sorted 排序 ')
# sort 和 sorted
# sort（）为 list 列表的方法，改变原有序列，
# sorted 对任意的序列进行排序，包括元组，因为返回一个新的序列。
li = [2, 45, 1, 67, 23, 10]  # 原始对象
print('排序之前-{}'.format(li))
li.sort()  # list的排序方法 直接修改的原始对象

print('sort() 排序之后-{}'.format(li))
# varList=sorted(li) # 默认 升序排列

varList = sorted(li, reverse=True)  # 降序排序， 默认为升序 false  # 不改变原有序列，返回新的序列
print('sorted() 排序之后 降序-{}'.format(varList))

tupArray = (2, 45, 1, 67, 23, 10)
varRs = sorted(tupArray, reverse=False)  # false 默认为升序
print('sorted() 排序之后-{}'.format(varRs))

print('-------- reverse()反转 ')
listA = [1, 2, 3, 4, 50, 12]
listA.reverse()  # 直接改变原来的列表
print('列表使用 reverse（） 之后{}'.format(listA))

print('-------- range()可创建一个整数列表，一般用在 for 循环中 ')
#  range(start, stop[, step])
for index in range(1, 9, 2):
    print(index)

print('-------- zip() ')
# zip() :就是用来打包的，会把序列中对应的索引位置的元素存储为一个元组
s1 = ['a', 'b', 'c']
s2 = ['你', '我', 'c他', 'peter']
s3 = ['你', '我', 'c他', '哈哈', '呵呵']
print(zip(s1))

print(list(zip(s1)))  # 压缩一个数据 为列表
print(list(zip(s1, s2)))  # 压缩一个数据 为列表
print(list(zip(s1, s2, s3)))  # 压缩一个数据 为列表

zipList = zip(s2, s3)  # 两个参数
print(list(zipList))

print('-------- zip()函数 案例')
def printBookInfo():
    '''
    zip 函数的使用
    :return:
    '''
    books = []  # 存储所有的图书信息
    id = input('请输入编号: 每个项以空格分隔\n')  # str
    bookName = input('请输入书名: 每个项以空格分隔\n')  # str
    bookPos = input('请输入位置: 每个项以空格分隔\n')

    idList = id.split(' ')
    nameList = bookName.split(' ')
    posList = bookPos.split(' ')

    bookInfo = zip(idList, nameList, posList)  # 打包处理
    for bookItem in bookInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo = {'编号': bookItem[0], '书名': bookItem[1], '位置': bookItem[2]}
        books.append(dictInfo)  # 将字典对象添加到list容器中
        pass
    for item in books:
        print(item)

# printBookInfo()

print('-------- enumerate()函数 用于将一个可遍历的数据对象')
# enumerate 函数用于将一个可遍历的数据对象,(如列表、元组或字符串)组合为一个索引序列，同时列出数据和
# 数据下标，一般用在 for 循环当中

# 主要就是对数据加 索引，放在遍历中

print('enumerate() 遍历 列表')
listObj=['a','b','c']
for item in enumerate(listObj):
    print(item) # 打印出来是元组
    print(type(item))
    pass
for index,item in enumerate(listObj, 5):  # 设置下标从 5 开始
    print(index,item) # 打印出来是 整形和字符串
    print(type(index),type(item))
    pass
print()

print('enumerate() 遍历 字典')
dicObj={}
dicObj['name']='李易峰'
dicObj['hobby']='唱歌'
dicObj['pro']='艺术设计'
print(dicObj)

for item in enumerate(dicObj):
    print(item)
    pass

for item in enumerate(dicObj):
    print(item[0])
    pass

for item in enumerate(dicObj):
    print(item[1])
    pass