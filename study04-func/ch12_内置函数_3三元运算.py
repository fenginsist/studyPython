# 三元运算
# python 没有 其他语言中的三元表达式，但是又类似的实现方法

# 其他语言中， 如 我原来的老本行 java
# int a = 1;
# String b = " "
# b = a > 1 ? "执行表达式或者什么值" ："再执行表达式或什么值" ；  # 如果 a > 1为 true 则 b = 问号左边，否则 = 问号右边

# 语法： result = 值1 if 条件 else 值2

a = 1
b = 2
c = 3

d = a if a < b else c  # 如果 a < b 为 true 则 d = if 左边的，否则 d = else 右边的

print(d)
