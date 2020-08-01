# 一、正则表达式
## 1. 正则表达式
正则表达式，英文名为Regular Expression，又称规则表达式。正则表达式通常被用来检索、替换那些符合某个模式(规则)的文本。

在主流操作系统（*nix[Linux, Unix等]、Windows、HP、BeOS等）、主流的开发语言（delphi、Scala、PHP、C#、Java、C++、Objective-c、Swift、VB、Javascript、Ruby以及Python等）、数以亿万计的各种应用软件中，都可以看到正则表达式优美的舞姿。

## 1. Python正则表达式
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。re 模块使 Python 语言拥有全部的正则表达式功能。同时，re 模块是用c语言写的，其匹配速度非常快。
其中compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

# 二、匹配字符串  re模块
re.match 尝试从字符串的起始位置匹配一个规则，匹配成功就返回match对象，否则返回None。可以使用group()获取匹配成功的字符串。  
语法：re.match(pattern, string, flags=0)  
参数说明：  
![](../images/study10/match参数.png) 

示例1（无标志位）：
```python
import re 
str = 'Python is the best language in the world’ 
# match 只能匹配以xxx开头的子符串，第一个参数是正则，第二个参数是需要匹配的字符串 
res = re.match('P',str) 
res.group() # 匹配成功使用group方法取出字符串 
'P'
```
示例2（有标志位）：
```python
import re 
str = 'Python is the best language in the world’ 
res = re.match(‘p’,str,re.I) 
res.group() 
'P' 
```
如果同时使用多个标志位使用|分割，比如re.I | re.M   
flags可选标志位  
![](../images/study10/flag标志位.png) 


1. .（点）的使用：匹配单个字符，除了换行符\ n 和 非字符 除外
2. [] 中括号的使用：匹配中括号中的任意一个字符
3. \d 的使用：匹配一个数字
4. \D 的使用：匹配一个非数字
5. \s 的使用：匹配一个空白字符 或者tab键
6. \S 的使用：匹配非空白字符
7. \w 的使用：匹配单词字符，即a-z、A-Z、0-9、_
8. \W 的使用：匹配非[a-z、A-Z、0-9]单词字符


# 三、匹配字符数量
1. * 的使用：匹配  前一个字符  出现0次或者无限次，即可有可无
2. + 的使用：匹配前一个字符出现 1 次或者无限次，即至少有 1 次
3. ？ 的使用：告诉引擎匹配前导字符 0 次或者一次，事实上表示前导字符是可以选择的
4. {min} 的使用：告诉引擎匹配前导字符min次
5. {min,} 的使用：告诉引擎匹配前导字符大于等于min次
6. {min,max} 的使用：告诉引擎匹配前导字符min次到max次 ，min和max必须都是非负整数



# 四、匹配原生字符串
python字符串中\作为转义字符开头，比如\n表示换行，\t表示tab键，为了表示\本身，再加一个\，成为\\形式 在python中表示路径‘G:\py资料\1-上课资料\4-正则表达式课件\html’
```python
mypath = 'G:\py资料\1-上课资料\4-正则表达式课件\html’ 
print(mypath) # 路劲输出异常 
G:\py资料-上课资料-正则表达式课件\html 

mypath = 'G:\\py资料\\1-上课资料\\4-正则表达式课件\\html’ 
print(mypath) # 将\转义之后正常 
G:\py资料\1-上课资料\4-正则表达式课件\html 
>>>

```
正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，那么使用编程语言表示的正则表达式里将需要4个反斜杠"\"。
在python中有原生字符串，在字符串前面加上r表示字符串中的\不转义。

# 五、 匹配开头和结尾
1. ^ 的使用：匹配字符串的开头
2. $ 的使用：匹配邮箱的结尾

![](../images/study10/匹配开头结尾.png)
示例：匹配163.com的邮箱地址
```python
import re 
# 正确地址 
ret = re.match('[\w]{4,20}@163\.com','python@163.com’) 
ret.group() 
'python@163.com’ 
# 不正确地址 
ret = re.match('[\w]{4,20}@163\.com','python@163.comsdsdds’) 
ret.group() 
'python@163.com’ 
# 通过$来限定结尾  
ret = re.match('[\w]{4,20}@163\.com$','python@163.comsdsdds’) 
ret.group() 
Traceback (most recent call last): 
	File "<stdin>", line 1, in <module> 
AttributeError: 'NoneType' object has no attribute 'group’ 

```

# 六、 匹配开头和结尾
![](../images/study10/分组匹配.png)



# 七、 匹配开头和结尾
## 1. compile 方法
compile 将正则表达式模式编译成一个正则表达式对象  
reg = re.compile(pattern) result = reg.match(string)  
等效于 result = re.match(pattern, string)  
使用re.compile()和保存所产生的正则表达式对象重用效率更高  

## 2. search 方法
search 在全文中匹配一次，匹配到就返回  
语法：re.search(pattern, string, flags=0)  
函数参数说明：  
![](../images/study10/匹配开头结尾.png)

## 3. findall 方法
findall 匹配所有返回一个列表，这个方法使用频率较高。
语法：findall(string[, pos[, endpos]])
参数说明：
![](../images/study10/findall.png)

## 4.sub
sub 将匹配到的数据进行替换
语法：sub(pattern, repl, string, count=0, flags=0)
参数说明：
![](../images/study10/sub.png)
##5. split
split 根据匹配进行切割字符串，并返回一个列表
语法：split(pattern, string, maxsplit=0, flags=0)
参数说明：
![](../images/study10/split.png)

# 八、贪婪模式与非贪婪模式
Python里数量词默认是贪婪的,总是尝试匹配尽可能多的字符,非贪婪则相反，总是尝试匹配尽可能少的字符。  
在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪.



# 小结

内容小结
元字符     说明                  正确    错误
\d      匹配任意单个数字           2      i、$
\D      匹配非数字                A/a     3
\w      匹配任意单个字母/数字/下划线  u       &
\W      匹配\w之外的任意单个字符    &       u
\s      匹配单个空格                       x
\S      匹配非空白，除空格，tab键之类 x
\n      匹配换行符
.       匹配任意单个字符【换行符除外】
\num    匹配前面引用的分组

多次的重复匹配
正则表达式     说明               正确   错误
A{3}          精准N次匹配        AAA     AA|A|AAAA
A{3,}          最少出现n次       AAA      A
\d{3,5}       约定出现最少次数和最大次数
\d*           可以出现0次至无限次 相当于{0,}
\d+           最少出现一次 相当于{1,}
\d?           最多出现一次 相当于{0,1} 1  12

定位匹配
正则表达式     说明            正确    错误
^A.*           头匹配          ABC    CBA
.*A$           尾部匹配        CBA     ABC
^A.*A$         全字匹配        ACCA    BAAA
字符的范围匹配
正则表达式     说明             正确   错误
A              精准匹配         A      a
x|y            匹配左右两边的字符 x/y   n
[xyz]          字符集合允许出现集合内任意单个字符 z、x、y     c、b
[a-z][A-Z][0-9]  字符范围
[^xyz][^0-9]     取反  集合内字符不允许出现的 0 A     y8

贪婪模式
在满足条件的情况下尽可能的去匹配多的字符串
实例:111222333  \d{6,8}
数据 ：小王出生于1997年   .*\d{4}年   贪婪模式

非贪婪模式
在满足条件的情况下尽可能的去匹配少的字符串
实例:111222333  \d{6,8}?
数据 ：小王出生于1997年   .*?\d{4}年   贪婪模式

