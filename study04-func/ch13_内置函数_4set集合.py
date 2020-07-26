# set 集合
# set（集合） 也是python中的一种数据类型，是一个无序且不重复的元素集合
# 不支持 索引 和 切片
# 类似于 字典，但是只有 key ，没有value

# 操作方法
# add()
# clear()
# difference()
# intersection()
# union()
# pop()
# discard()
# update()


print('------ 创建集合')
# 创建集合
dict1 = {}  # dict字典
set1 = {1, 2, 3, }  # set 集合
print(type(dict1))  # <class 'dict'>
print(type(set1))  # <class 'set'>
print(set1)  # {1, 2, 3}

print('------ 添加操作')
# 添加操作
set1.add('python')
set1.add('python1')
print(set1)

print('------ 清空操作')
# 清空操作
set1.clear()
print(set1)  # 输出 set()

print('------ 差集操作 等价于 set2 - set3')
# 差集操作  等价于 set2 - set3
set2 = {2, 3, 4}
set3 = {2, 3, 9}

res = set2.difference(set3)

print(set2-set3)
print(res)

print('------ 交集操作  等价于 &')
print(set2.intersection(set3))
print(set2 & set3)

print('------ 并集操作  等价于 |')
print(set2.union(set3))
print(set2 | set3)

print('------ pop() 操作')
# pop 集合pop随机移除某个元素并且获取那个参数,集合pop没有参数
print(set2)
set2.pop()
print(set2)


print('------ discard() 操作')
# discard 移除指定元素
set2.discard(3)
print(set2)

print('------ update() 操作')
# update 更新集合
set2.update(set3)
print(set2)


