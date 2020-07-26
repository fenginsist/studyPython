import re

'''
通过python中的 re模块 的使用最终掌握正则表达式的常用匹配规则
group(num) 可以获取匹配的数据  如果有多个匹配结果的话 那么会以元组的形式 存放到group对象中，此时我们可以通过下标去获取
groups()  返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''

print('-----------------------测试 精准匹配下，忽略大小写')
strData = 'Python is the best language in the world'
# match 只能匹配以xxx开头的子符串，第一个参数是正则，第二个参数是需要匹配的字符串
res = re.match('python', strData, re.I | re.M)  # 第三个参数 I 表示忽略大小写， M 表示多行匹配
if res:
    print('匹配成功...')
    print(res)
    print(res.group())  # 获取目标字符串中  匹配的内容
else:
    print('匹配失败...')

print('-----------------------可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式')
res2 = re.match('(.*) is (.*?) .*', strData, re.I | re.M)   # (.*) is (.*?) .* 匹配的 是 Python the
if res2:
    print('匹配成功...')
    print(res)            # <re.Match object; span=(0, 6), match='Python'>
    print(res2.groups())  # ('Python', 'the')
    print(res2.group(1))  # Python
    print(res2.group(2))  # the
else:
    print(res2.group())  # 如果匹配失败 是没有group函数的 因为是一个空对象None
    print(res2)
    print('匹配失败...')
