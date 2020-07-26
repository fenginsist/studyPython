import re

print('----------- .（点）的使用：匹配单个字符，除了换行符\ n 和 非字符 除外')
# .（点） 的使用；  匹配规则是除了 换行符之外的字符
data = 'a2aaa'
pattern = '..'
res = re.match(pattern, data)
print(res.group())

print('----------- .（点）的应用')
names = '李达', '李明', '小王', '小李'
pattern = '李.'  # 匹配规则
for name in names:
    res = re.match(pattern, name)
    if res:
        print(res.group())

print('----------- [] 中括号的使用：匹配中括号中的任意一个字符')
# []中括号的使用  匹配规则是：匹配中括号中的任意一个字符
print('-- 测试一：')
str1 = 'hello'
res1 = re.match('[he]', str1)
print(res1.group())

print('-- 测试二：')
str2 = 'ehello'
res2 = re.match('[He]', str2)
print(res2.group())

print('-- 测试三：')
str3 = 'ohello'
res3 = re.match('[He]', str3)
try:
    print(res3.group())
except Exception as msg:
    print('匹配失败')
    print(msg)
    pass
'''
通过测试一、二、三
说明：只匹配 str 的第一个字符
'''

print('-- 测试四：')
pattern = '[abc]'  # [abc]代表可以匹配a或者b或者c,  使用中括号括起来的内容, 代表一个集合，代表匹配集合内的任意一个字符
# pattern='[a-g]'  # 可以简写一个范围 abcdefg

datas = 'a', 'b', 'c', 'e', 'wyw'
for data in datas:
    result = re.match(pattern, data)
    if result:
        print('匹配成功 %s' % result.group())

print('----------- \d 的使用：匹配一个数字')
# \d 匹配一个数字  0-9
data = '12345abcdef'
print(re.match('\d\d\d', data).group())

print('----------- \D 的使用：匹配一个非数字')
# \D 匹配一个非数字
data = 'W12345abcdef'
print(re.match('\D', data).group())
try:
    print(re.match('\D\D', data).group())
except Exception as msg:
    print('匹配失败：原因：', msg)

print('----------- \s 的使用：匹配一个空白字符 或者tab键')
# \s 匹配一个空白字符 或者tab键
data = '  hello'
print(re.match('\s\s', data).group())

print('----------- \S 的使用：匹配非空白字符')
# \S 匹配非空白字符
data = 'Python  hello'
print(re.match('\S\S\S\S\S', data).group())

print('----------- \w 的使用：匹配单词字符，即a-z、A-Z、0-9、_')
# \w 匹配单词字符，即a-z、A-Z、0-9、_
data = '_2Yssdf'
print(re.match('\w\w\w\w', data).group())

print('----------- \W 的使用：匹配非[a-z、A-Z、0-9]单词字符')
# \W 匹配非[a-z、A-Z]单词字符
data = '@$ # _2Y0ssdf'
print(re.match('\W\W\W\W', data).group())
