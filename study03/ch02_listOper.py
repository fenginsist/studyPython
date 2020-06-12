# 列表操作
'''
list:python当中非常重要的数据结构，是一种有序的数据集合
特点：
1：支持增删改查
2：列表中的数据是可以变化的【数据项可以变化，内存地址不会改变】
3:用[] 来表示列表类型，数据项之间用逗号来分割，注意：数据项可以是任何类型的数据
4：支持索引和切片来进行操作
'''

# 列表定义
li = []  # 空列表
listA = [1, 2, 3, '你好']

print('------------------1、列表长度、类型-----------------------')
# 打印列表类型 和 长度
print(type(listA))
print(len(listA))  # len函数可以获取到列表对象中的数据个数
strA = '我喜欢python'
print(len(strA))

print('------------------2、列表 遍历：通过下标和切片取值-----------------------')
listB = ['abcd', 785, 12.23, 'qiuzhi', True]
print(listB)  # 输出完整的列表
print(listB[0])  # 输出第一个元素
print(listB[1:3])  # 从第二个开始到第三个元素
print(listB[2:])  # 从第三个元素开始到最后所有的元素
print(listB[::-1])  # 负数从右像左开始输出
print('遍历', listB)
print(listB * 3)  # 输出多次列表中的数据【复制】

print('------------------3、列表 增加-----------------------')
print('追加之前', listB)
listB.append(['fff', 'ddd'])  # 追加操作， 插入的是一个
listB.append(8888)
print('追加之后', listB)

listB.insert(1, '这是我刚插入的数据')  # 插入操作 需要执行一个位置插入
print(listB)

print('------------------4、列表 强转-----------------------')
rsData = list(range(10))  # 强制转换为list对象
print(type(rsData))
print(rsData)

print('------------------5、列表 批量添加-----------------------')
listB.extend(rsData)  # 拓展  等于批量添加
listB.extend([11, 22, 33, 44])
print(listB)

print('------------------6、列表 修改-----------------------')
print('修改之前：', listB)
listB[0] = 333.6
print('修改之后：', listB)

print('------------------7、列表 删除,两种删除方式：关键字、函数-----------------------')
listC = list(range(10, 50))
print('删除之前%s' % listC)
del listC[0]  # 删除列表中第一个元素
del listC[1:3]  # 批量删除多项数据 slice
print('删除之后%s' % listC)

listC.remove(20)  # 移除指定的元素  参数是具体的数据值
print('删除指定的数据20%s' % listC)

listC.pop(1)  # 移除制定的项  参数是索引值
print('删除指定的数据下标%s' % listC)

print('------------------8、列表 查找-----------------------')
print(listC.index(11))  # 返回的是一个索引下标
print(listC.index(25, 5, 16))  # 查找 25 ，从下标为5开始查找 步长为16的范围 。返回的是一个索引下标,

print('------------------9、统计元素出现的次数-----------------------')
print(listC.count(22))
