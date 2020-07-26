# 共用方法 +  *  in

print('---------------合并: 字符串、列表 + -----------------')
strA = '人生苦短'
strB = '我用python'
print('字符串合并', strA + strB)
listA = list(range(10))
listB = list(range(11, 20))
print('列表合并', listA + listB)

print('---------------复制: 字符串、列表  * -----------------')
print(strA * 3)
print(listB * 3)

print('---------------存在: 对象是否存在 结果返回一个bool值  in -----------------')
print('是否存在字符串中：', '人' in strA)  # True
print('是否存在列表中：', 22 in listA)  # False
dictA = {'name': 'peter'}
print('是否存在某个key：', 'name' in dictA)
print('是否存在某个value：', 'peter' in dictA)

print('---------------查看长度: len() -----------------')
print('字符串长度：', len(strA))
print('列表长度：', len(listA))
print('字典长度：', len(dictA))
