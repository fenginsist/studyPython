# 逻辑运算符 and or  not 共 3 个

# and 逻辑运算符 条件比较严格,全true 才为 true
# 定义四个变量
a, b, c, d = 23, 18, 10, 3
print(a + b > c and c < d)  # false
print(c > d and a > b)  # true

# or 逻辑运算符 全 false 才为 false
print('-----------or--------------')
print(a < b or b > d)  # true
print(a < b or b < d)  # false

# not 逻辑运算符 True 为False，False 为 True
print('-----------not--------------')
print(not a > b)  # false
print(not a < b)  # true

# 优先级
print('-----------priority--------------')
# （） > not > and > or
print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)
