import re

'''
compile re模块中的编译方法 可以把一个字符串编译成字节码
优点: 在使用正则表达式进行 match的操作时，python会将 字符串 转为正则表达式对象，
而如果使用 complie 则只需要完成一次转换即可，以后再使用模式对象的话 无需重复转换，
'''

print('------------------ re.compile（\'正则表达式\'）:传入正则表达式，返回正则表达式对象')
reobj = re.compile('\d{4}')
# 开始去使用模式对象reobj
rs = reobj.match('1235678')
print(rs.group())

# 等价于 下面的使用
print(re.match('\d{4}', '1235678').group())

print('------------------ re.search 在全文中匹配一次，匹配到就返回')
# re.search  规则是:在全文中匹配一次，匹配到就返回
data = '我爱伟大的祖国,I love China,China is a great country'
rs = re.search('China', data)
print(rs)
print(rs.group())
print(data[19])
print(data[20])

print('------------------ re.findall() 查询字符串中某个正则表达式全部的非重复出现的情况 返回的是一个符合正则表达式的结果列表')
# re.findall() 查询字符串中某个正则表达式全部的非重复出现的情况 返回的是一个符合正则表达式的结果列表
data = '华为是华人的骄傲华侨'
rs = re.findall('华.', data)
research = re.search('华.', data)
print(rs)  # ['华为', '华人', '华侨']
print(research)  # <re.Match object; span=(0, 2), match='华为'>
print(research.group())  # 华为

print('------------------ 改造一下使用compile，使用正常表达式对象进行匹配，提高了速度')
# 改造一下使用compile
reobj = re.compile('华.')  # 创建一次正则对象转换
print(reobj.search(data))
print(reobj.findall(data))

print('------------------ re.sub 实现目标的搜索和替换; re.subn 实现目标的搜索和替换  还返回被替换的数量 以元组形式')
# re.sub 实现目标的搜索和替换
# re.subn 实现目标的搜索和替换  还返回被替换的数量 以元组形式
dataS = 'Python是很受欢迎的编程语言Python'
pattern = '[a-zA-Z]+'  # 字符集的范围 + 号 代表 前导字符模式出现1次以上
res = re.sub(pattern, 'Java', dataS)
resn = re.subn(pattern, 'Java', dataS)
print(res)
print(resn)

print('------------------ re.split  实现分割字符串')
# re.split  实现分割字符串
data = '百度,腾讯,阿里,华为,360'
rs = re.split(',', data)
print(type(rs))
print(rs)
