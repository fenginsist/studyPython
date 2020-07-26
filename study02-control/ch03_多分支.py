'''
多分支的选择【多个条件】
 if  条件表达式: 比较运算符 逻辑运算符 /复合的条件表达式
    代码指令
    pass
 elif 条件表达式:
    代码指令
    pass
 elif 条件表达式:
    代码指令
    pass
 ......
 else:
    代码指令
    pass

特征:
1.只要满足其中一个分支，就会退出本层if语句结构【必定会执行其中一个分支】
2.至少有2中情况可以选择
elif 后面必须的写上条件和语句
else 是选配，根据实际的情况来填写
'''

score = int(input('请输入您的成绩：'))
print(type(score))

if score > 90:
    print('您的成绩是A等级')
    pass
elif score >= 80:
    print('您的成绩是B等级')
    pass
elif score >= 70:
    print('您的成绩是C等级')
    pass
elif score >= 60:
    print('您的成绩是D等级')
    pass
else:
    print('您的成绩不合格')

print('程序结束了。。。')
