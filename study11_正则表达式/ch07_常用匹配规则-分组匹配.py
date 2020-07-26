import re

print('------------------ | 的使用：竖线 匹配左右任意一个表达式  实际上是一个  或 的关系')
# |  竖线 匹配左右任意一个表达式  实际上是一个  或 的关系
string = 'wywsqpeng'
rs = re.match('(wywsqpeng|wywsqpeng888)', string)
rs2 = re.match('(wywsqpeng888|wywsqpeng)', string)
print(rs.group())
print(rs2.group())

print('------------------ (ab) 的使用：分组匹配  将括号中字符作为一个分组')
# (ab) 分组匹配  将括号中字符作为一个分组
# 匹配电话号码  xxxx-123456789
# ^ 有两种含义 1：以xxxx开头  2:否定 取反
res = re.match('([^-]*)-(\d*)', '021-456213987')
print(type(res.group()))  # <class 'str'>
print(type(res.groups()))  # <class 'tuple'>
print(res.group())  # 021-456213987
print(res.groups())  # ('021', '456213987')
print(res.group(0))  # 021-456213987
print(res.group(1))  # 021
print(res.group(2))  # 456213987

print('------------------ \\num 的使用：引用分组num匹配到的字符串')
# \num 的使用  引用分组num匹配到的字符串
htmlTag = '<html><h1>测试数据</h1></html>'
res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag)
# 第一个 (.+) 称为编组 1  ， 第二个 (.+) 称为编组2   。所以 在后面的 可以使用\2 \1 选择对应的编组
print(res.group(1))
print(res.group(2))
print(res.group(3))

print('------------------ 分组: 别名的使用 (?P<名字>)  /  如何使用别名 (?P=引用的名字)')
# 分组 别名的使用 (?P<名字>)
# 如何使用别名 (?P=引用的名字)
data = '<div><h1>www.baidu.com</h1></div>'
res1 = re.match(r'<(\w*)><(\w*)>.*</(\w*)></(\w*)>', data)
res2 = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', data)
print('正常的模式', res1.group())
print('使用别名模式', res2.group())
