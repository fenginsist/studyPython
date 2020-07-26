import re

print('--------------- ^ 的使用：匹配字符串的开头')
# ^ 匹配字符串的开头
result = re.match('^P.*', 'Python is langage')
result2 = re.match('^P\w{5}', 'Python is langage')
if result:
    print(result.group())  # Python is langage
    pass
if result2:
    print(result2.group())  # Python
    pass

print('--------------- $ 的使用：匹配邮箱的结尾')
# $ 匹配邮箱的结尾
result1 = re.match('[\w]{5,15}@[\w]{2,5}.com$', 'myfunckmail@mail.com')
result2 = re.match('[\w]{5,15}@[\w]{2,5}.com$', 'myfunckmail@mail.comTest')
if result1:
    print(result1.group())
    pass
if result2:
    print(result2.group())
    pass
