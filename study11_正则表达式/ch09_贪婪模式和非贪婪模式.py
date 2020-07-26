import re

# 贪婪模式
# 默认的匹配规则
# 在满足条件的情况下尽可能多的去匹配到数据

print('-----------------默认的贪婪模式:')
rs = re.match('\d{6,9}', '111222333')
print(rs.group())

print('非贪婪模式:')
# 非贪婪模式
# 在满足条件的情况下尽可能【少】的去匹配到数据
rs = re.match('\d{6,9}?', '111222333')
print(rs.group())

print('-----------------默认的贪婪模式:')
content = 'aacbacbc'
pattern = re.compile('a.*b')
result = pattern.search(content)
print('贪婪模式%s' % result.group())

print('非贪婪模式:')
content = 'aacbacbc'
pattern = re.compile('a.*?b')  # 非贪婪模式匹配
result = pattern.search(content)
print('非贪婪模式%s' % result.group())

print('-----------------测试:')
data = '小王出生于1997年'
patt = '.*(\d{4})年'
print(re.match(patt, data).group(1))
