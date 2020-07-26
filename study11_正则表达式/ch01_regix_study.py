# 通过 python 中的 re 模块去学习并使用 正则表达式的基本知识点

import re

'''
re.match() 尝试 从字符串的起始位置  匹配一个规则  ，匹配成功就返回match对象，否则返回 None。
可以使用group()获取匹配成功的字符串。
'''

data = 'Python is the best language in the world'
result = re.match('Python', data)  # 最简单的一种匹配方式，精确匹配
print(type(result))  # <class 're.Match'>
print(result.group())  # 匹配成功使用group方法取出字符串  Python
