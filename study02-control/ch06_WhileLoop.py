'''
循环的分类
while 语法结构
while 条件表达式:
    代码指令
'''
'''
语法特点
1.有初始值
2.条件表达式
3.变量【循环体内计数变量】的自增自减, 否则会造成死循环
使用条件：循环的次数不确定，是依靠循环条件来 结束
目的: 为了将相似或者相同的代码操作变得更加简洁，使得代码可以重复利用
'''

'''
end 关键字：
end 是print函数中的关键字。
在while、for循环中，每次输出都是换行的。加入end，使用end=“”中的内容代替换行，分隔每次循环输出内容
'''

# 案例1  输出1-10之间的数据
index = 1
while index <= 10:
    print(index)
    index += 1

# 案例2  打印九九乘法表  循环的嵌套
# 打印正三角
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print('%d*%d=%d' % (row, col, row * col), end=' ')
        col += 1
        pass
    print()
    row += 1
    pass

# 打印倒三角
row = 9
while row >= 1:
    col = 1
    while col <= row:
        print('%d*%d=%d' % (row, col, row * col), end=' ')
        col += 1
        pass
    print()
    row -= 1
    pass

# 案例3 打印直角三角形
# 正三角
row = 1
while row <= 7:
    col = 1
    while col <= row:
        print('*', end=' ')
        col += 1
        pass
    print()
    row += 1
    pass

# 倒三角
row = 7
while row >= 1:
    col = 1
    while col <= row:
        print('*', end=' ')
        col += 1
        pass
    print()
    row -= 1

# 案例4 打印等腰三角形
# 第一行1个 第二行3个 第三行5个 第四行7个
row = 1
while row <= 5:
    col = 1
    while col <= 5 - row:  # 控制打印左边空格的数量
        print(' ', end=' ')
        col += 1
        pass
    k = 1
    while k <= 2 * row - 1:  # 控制打印 * 号
        print('*', end=' ')
        k += 1
        pass
    print()
    row += 1
