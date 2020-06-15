'''
猜年龄小游戏，有三点需求
1.允许用户最多尝试3次
2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y， 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
3.如何猜对了，就直接退出
目的：演练 while 和 if 的使用，综合运用
'''
print('------------------作业一：------------------')
times = 0
while times <= 3:
    ageInput = int(input('请输入您猜测的年龄：'))
    age = 25
    if ageInput == age:
        print('恭喜您，猜对了')
        break
        pass
    elif ageInput > 25:
        print('猜大了')
        pass
    else:
        print('猜小了')
    times += 1
    if times == 3:
        choose = input('想继续猜吗？ Y/N？')
        if choose == 'Y' or choose == 'y':
            times = 0
            pass
        elif choose == 'N' or choose == 'n':
            times = 4
            pass
        else:
            print('请不要乱输入')
            pass
        pass



print('------------------作业二：------------------')
'''
小王身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，并根据BMI指数：
低于18.5   过轻
18.5-25： 正常
25-28：    过重
28-32：    肥胖
高于32：  严重肥胖
用if-elif判断并打印结果
'''

weight = 80.5
high = 1.75
bmi = weight / (high * high)
print('BMI的数据是%d'%(bmi))
if bmi < 18.5:
    print('过轻')
    pass
elif bmi >= 18.5 and bmi < 25:
    print('正常')
    pass
elif bmi >= 25 and bmi < 28:
    print('过重')
    pass
elif bmi >= 28 and bmi < 32:
    print('肥胖')
    pass
elif bmi >= 32:
    print('严重肥胖')
