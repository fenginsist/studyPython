'''
for循环
语法特点: 遍历操作，依次的取集合容器中的每个值
for 临时变量 in 容器:
    执行代码块
'''
print('--------------for循环： 打印字符串------------------')
tags = '我是一个中国人'  # 字符串类型本身就是一个字符类型的集合
for item in tags:
    print(item, end=' ')
    pass

print()
print('--------------for循环： range函数，计算1到100的加和------------------')
'''
range 此函数可以生成一个数据集合列表
range(起始:结束:步长)  步长不能为0
'''
print(type(range(1, 100)))
sum = 0
for data in range(1, 101):  # 左边包含  右边不包含
    sum += data  # 求累加和
    print(data, end=' ')
    pass
print()
print('1+...+100=', sum)

print('--------------for循环： 嵌套if-else------------------')
for data in range(50, 201):
    if data % 2 == 0:
        print("%d是偶数" % data)
        pass
    else:
        print("%d是奇数" % data)
pass

'''
break和continue
break 代表中断结束，满足条件直接的结束本层循环
continue:结束本次循环，继续的进行下次循环（当continue的条件满足的时候，本次循环剩下的语句将不在执行
后面的循环继续）
这两个关键字只能用在循环中使用（while、loop）
'''
print('--------------for循环： break的使用------------------')
sum = 0
for item in range(1, 51):
    if sum > 100:
        print('循环执行到%d就退出来了' % item)
        break  # 退出循环体
        pass
    sum += item
    pass
print("sum=%d" % sum)

print('--------------for循环： continue的使用------------------')
for item in range(1, 100):  # 求出来奇数
    if item % 2 == 0:
        continue
        print('在continue的额后面会不会执行呢')  # 这句话不会执行
        pass
    print(item)
    pass

print('--------------for循环： 练习 break 和 continue------------------')
for item in 'i love python':
    if item == 'e':
        break  # 彻底终端循环，
        # continue
    print(item, end=' ')

# break 打印出 i   l o v
# continue 打印出 i   l o v   p y t h o n

print()
print('--------------while循环： 练习 break 和 continue------------------')
index = 1
while index <= 100:
    index += 1
    if index > 20:
        break
        pass
    print(index)

print('--------------for循环案例： 打印九九乘法表------------------')
# 案例1 打印九九乘法表  循环的嵌套
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end=' ')
        pass
    print()
    pass

print('--------------for循环案例： for---else使用------------------')
# for---else 使用
for item in range(1, 11):
    print(item, end=' ')
    pass
else:
    print('就是上面循环当中，只要是出现了break 那么else 的代码将不再执行')

'''
for-else 使用，密码用户三次机会登录
'''
account = 'wyw'
pwd = '123'
for i in range(3):
    zh = input('请输入账号')
    pd = input('请输入密码')
    if account == zh and pwd == pd:
        print('登录成功！！')
        break
    pass
else:
    print('您的账号已经被系统锁定。。。')

print('--------------while循环案例： while---else使用------------------')
index = 1
while index <= 10:
    print(index)
    if index == 6:
        break
        pass
    index += 1
    pass
else:
    print('else 执行了么') # 不会打印这句
