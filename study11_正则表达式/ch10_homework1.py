import re

print('-----------1、长度为8-10的用户密码（以字母开头 ,包含字母、数字、下划线）')
# 1、长度为8-10的用户密码（以字母开头 ,包含字母、数字、下划线）
pattern = re.compile('[a-zA-Z][a-zA-Z0-9_]{7,9}')
rs = pattern.match('sds121212dssssssdddddddddddddd')
print(rs.group())
try:
    rs1 = pattern.match('sd')
    print(rs1.group())
except Exception as msg:
    print('匹配失败，原因：', msg)

print('-----------2、验证用户名，长度为6-18位的英文字母组成')
# 2、验证用户名，长度为6-18位的英文字母组成
pattern = re.compile('[a-zA-Z]{6,18}')
res = pattern.match('asasdddd')
print(res.group())
try:
    rs1 = pattern.match('abcdefghijklmnopqrstuvwxyz')
    print(rs1.group())
except Exception as msg:
    print('匹配失败，原因：', msg)

print('-----------3、邮箱验证126，163邮箱：6~18个字符，可使用字母、数字、下划线，需以字母开头')
# 3、邮箱验证126，163邮箱：6~18个字符，可使用字母、数字、下划线，需以字母开头
try:
    result = re.match('[a-zA-Z][a-zA-Z0-9_]{5,17}@126.com', 'abcdef@126.com')
    print(result.group())
except Exception as msg:
    print('匹配失败，原因：', msg)
    pass

try:
    result = re.match('[a-zA-Z][a-zA-Z0-9_]{5,17}@126.com', 'abcdefghijklmnopqrst@126.com')
    print(result.group())
except Exception as msg:
    print('匹配失败，原因：', msg)

print('-----------4、匹配手机号码(11位数字)')
# 4、匹配手机号码(11位数字)
# 移动号码段:139、138、137、136、135、134、150、151、152、157、158、159、182、183、187、188、147
# 联通号码段:130、131、132、136、185、186、145
# 电信号码段:133、153、180、189


# 5、python中的re模块匹配规则默认是贪婪模式还是非贪婪模式，两种模式的区别？
# 默认贪婪模式，

print('-----------6、Python 中使用re模块macth方法匹配文本时，如果需要忽略文本大小写进行匹配，如何操作')
# 6、Python 中使用re模块macth方法匹配文本时，如果需要忽略文本大小写进行匹配，如何操作？
re.match('', '', re.I)
'''
re.I 使匹配对大小写不敏感
re.L 做本地化识别（locale-aware）匹配
re.M 多行匹配，影响 ^ 和 $
re.S 使 . 匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''

print('-----------7、写一个正则匹配python变量名')
# 7、写一个正则匹配python变量名
# 变量名：不能以数字开头，变量名只能包含字母，数字，下划线
result = re.match('[a-zA-Z][a-zA-Z0-9_]+', 'asasssasaassdabcdefghijklmnopqrstuvwsyz')
print(result.group())

result1 = re.match('[a-zA-Z][a-zA-Z0-9_]+\w', 'asasas122345678sdsda12121290')
print(result1.group())

# 8、写一个正则匹配路径 "C:\myfile\myfile"
