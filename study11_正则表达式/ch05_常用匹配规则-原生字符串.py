import re

print('-----------------------输出转义字符的原生字符串')
mypath = 'G:\py资料\1-上课资料\4-正则表达式课件\html'
mypath2 = 'G:\\py资料\\1-上课资料\\4-正则表达式课件\html'
print(mypath) # G:\py资料-上课资料-正则表达式课件\html
print(mypath2) # G:\py资料\1-上课资料\4-正则表达式课件\html

print('-----------------------对转义字符进行匹配正则表达式')
try:
    res = re.match('c:\\a.txt','c:\\a.txt')
    print(res.group())
except Exception as msg:
    print('匹配失败， 原因：', msg)
    pass
# 需要添加转义字符
res2 = re.match('c:\\\\a.txt','c:\\a.txt')
if res2:
    print(res2.group())
    pass

print('-----------------------r 关键字 不转义')
res3 = re.match(r'c:\\a.txt','c:\\a.txt')
if res3:
    print(res3.group())
    pass

'''
正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，
那么使用编程语言表示的正则表达式里将需要4个反斜杠"\"。

在python中有原生字符串，在字符串前面加上r表示字符串中的\不转义。

'''



