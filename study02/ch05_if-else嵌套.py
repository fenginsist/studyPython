# if-else 的嵌套使用

# 一个场景需要分阶段或者层次，做出不同的处理
# 要执行内部的 if 语句 一定要外部的 if 语句满足条件才可以
score = int(input('请输入您的学分：'))

if score > 10:
    grade = int(input('请输入您的成绩：'))
    if grade >= 80:
        print('您可以升班了，恭喜您！！')
        pass
    else:
        print('很遗憾，您的成绩不达标！！')
        pass
    pass
else:
    print('您的表现有点差，学分成绩不达标。无法升班！！')
    pass
