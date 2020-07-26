import re

print('---------作业一：')
# 1、'Save your heart for someone who cares' 请使用正则将文本中的"s"替换成"S",请写Python代码完成匹配替换。

data = 'Save your heart for someone who cares'
res = re.subn('s', 'S', data)
print(res)

print('---------作业二：')
# 2、'<span>三生三世，十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>' 请使用正则将<span>标签中的全部内容匹配出来
# ,请写Python代码完成匹配

data = '<span>三生三世，十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>'

# 分组别名的用法
print('分组别名的用法:')
patternNick = r'<(?P<A>\w*)>(.*)</(?P=A)><(?P=A)>(.*)</(?P=A)><(?P=A)>(.*)</(?P=A)>'
reobj = re.compile(patternNick)
result = reobj.findall(data)
print(result)

print('非分组别名的用法:')
reobj=re.compile(r'<span>(.*)</span><span>(.*)</span><span>(.*)</span>')
rs = reobj.findall(data)
print(rs)


