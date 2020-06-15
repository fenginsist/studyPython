# 字典操作
'''
字典：也是python中重要的数据类型，字典是有 键值对 组成的集合，通常使用 键来访问数据，效率非常高，和list一样 支持对数据的添加、修改、删除
特点：
1：不是序列类型 没有下标的概念，是一个无序的 键值集合，是内置的高级数据类型
2：用{} 来表示字典对象，每个键值对用逗号分隔
3：键 必须是不可变的类型【元组、字符串】 值可以是任意的类型
4: 每个键必定是惟一的，如果存在重复的键，后者会覆盖前者
'''

print('---------------------1、字典创建------------------------')
dictA = {}  # 空字典
dictA = {'pro': '艺术', 'school': '山东中医药大学'}
dictA['name'] = '李易峰'  # key:value
dictA['age'] = 30
dictA['pos'] = '歌手'

# 结束添加
print('遍历：', dictA)
print('dictA类型：', type(dictA))
print('字典长度：', len(dictA))

print('---------------------2、字典修改:两种方式------------------------')

dictA['name'] = '谢霆锋'
dictA['school'] = '香港大学'
print('修改方式一修改之后：', dictA)

dictA.update({'age': 99})
dictA.update({'height': 99})  # 可以 更新 和 添加
print('修改方式二修改之后：', dictA)

print('---------------------3、字典获取------------------------')
# 获取所有的 键
print('获取所有的 键:', dictA.keys())
# 获取所有的 值
print('获取所有的 值:', dictA.values())
# 获取所有的 键和值
print('获取所有的 键和值:', dictA.items())  # 每个 为 元组

for key, value in dictA.items():
    print('%s == %s' % (key, value))
    pass

print('---------------------4、字典 删除:关键字 和 pop() 方法------------------------')
print('删除之前：', dictA)
del dictA['name']
dictA.pop('age')
print('删除之后：', dictA)

print('---------------------5、字典  排序（进阶）------------------------')
# 如何排序， 按照 key 排序
print('按照 key 排序', sorted(dictA.items(), key=lambda item: item[0]))
# 按照 value 排序
# print('按照 value 排序', sorted(dictA.items(), key=lambda item: item[1]))
