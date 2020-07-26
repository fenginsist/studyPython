import re

print('----------- * 的使用：匹配  前一个字符  出现0次或者无限次，即可有可无')
# *  匹配前一个字符出现0次或者无限次，即可有可无,没匹配上也不会报错。

try:
    result = re.match('[A-Z][A-Z]', 'Ay')
    print(result.group())
except Exception as msg:
    print('匹配失败，原因：', msg)
    pass
result1 = re.match('[A-Z][A-Z]*', 'Ay')
result2 = re.match('[A-Z][a-z]*', 'Ay')
result3 = re.match('[A-Z][a-z]*', 'Ayadfvsfvsvsvsva')
result4 = re.match('[A-Z][a-z]*', 'AyadfvsfvSSvsvsva')

print(result1.group())
print(result2.group())
print(result3.group())
print(result4.group())

print('----------- + 的使用：匹配前一个字符出现 1 次或者无限次，即至少有 1 次')
# +  匹配前一个字符出现1次或者无限次，即至少有1次

try:
    res1 = re.match('[A-Z]+', 'mYnnnnaisfjksg')
    print(res1.group())
except Exception as msg:
    print('匹配失败，原因：', msg)
    pass

res2 = re.match('[A-Z]+', 'MYnnnnasfjksg')
print(res2.group())  # MY
res3 = re.match('[A-Z]+', 'MYNAMEasfjksg')
print(res3.group())  # MYNAME
res4 = re.match('[a-zA-Z]+', 'MYNAMEasfjksg') # 这个加号 指 字符串中 属于[a-zA-Z] 这个的即可
print(res4.group())  # MYNAMEasfjksg

print('----------- 应用：匹配符合规范【规则是：不能以数字开头，只能包含字母、数字、下划线】的 python 变量命名')
# 匹配符合规范【规则是：不能以数字开头，只能包含字母、数字、下划线】的 python 变量命名
result1 = re.match('[a-zA-Z_]+\w', 'asassdsd112')
result2 = re.match('[a-zA-Z_]+\w', '_name')
print(result1.group())
print(result2.group())
try:
    result3 = re.match('[a-zA-Z_]+\w', '11name')
    print(result3.group())
except Exception as  msg:
    print('匹配失败，原因：', msg)
    pass
result4 = re.match('[a-zA-Z_]+\w', '_na87me')
print(result4.group()) # _na8

print('----------- ？ 的使用：告诉引擎  匹配前导字符 0 次或者一次，事实上表示前导字符是可以选择的')
# ？ 告诉引擎匹配前导字符 0 次或者一次，事实上表示前导字符是可以选择的
result1 = re.match('[a-zA-Z][0-9]?', 'nameFunck99m_e')
result2 = re.match('[a-zA-Z]+[0-9]?', 'nameFunck99m_e')
print(result1.group())
print(result2.group())

print('----------- {min} 的使用：告诉引擎匹配前导字符min次')
# {min,max}  告诉引擎匹配前导字符min次到max次 ，min和max必须都是非负整数
# {count} 精确匹配
result = re.match('\d{4}', '1233422') # \d 等于 4 位
if result:
    print('匹配成功: {}'.format(result.group()))  #
    pass

print('----------- {min,} 的使用：告诉引擎匹配前导字符大于等于min次')
result2 = re.match('\d{4,}', '1233426861842') # \d 大于 4 位
if result2:
    print('匹配成功: {}'.format(result2.group()))
    pass

print('----------- {min,max} 的使用：告诉引擎匹配前导字符min次到max次 ，min和max必须都是非负整数')
result3 = re.match('\d{4,8}', '1233426861842') # \d 至少 4 位 ， 小于等于8位
if result3:
    print('匹配成功: {}'.format(result3.group()))
    pass

print('----------- 应用：匹配邮箱demo   格式xxxxxx@163.com')
# 匹配邮箱demo   格式xxxxxx@163.com
try:
    result = re.match('[a-zA-Z0-9]{6,11}@163.com', 'acavavav@163.com')
    print('匹配成功: {}'.format(result.group()))
except Exception as msg:
    print('匹配失败，原因：', msg)
    pass

try:
    result1 = re.match('[a-zA-Z0-9]{6,11}@163.com', 'acaddddddvavav@163.com')
    print('匹配成功: {}'.format(result1.group()))
except Exception as msg:
    print('匹配失败，原因：', msg)
    pass

print('----------- 应用：匹配电话号码 11位')
# 匹配电话号码 11位
result = re.match('[0-9]{11}', '17862970812')
if result:
    print('匹配成功: {}'.format(result.group()))
    pass
result1 = re.match('[0-9]{11}', '1786scfs2970812')
if result1:
    print('匹配成功: {}'.format(result1.group()))
    pass







