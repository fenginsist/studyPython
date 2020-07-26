'''
多分支 多条件的演练
猜拳击的小游戏
0:石头 1:剪刀 2:布
'''

# 直接导入产生随机数的模块
import random

# 计算机  人
person = int(input('请出拳:[0:石头 1:剪刀 2:布]'))
computer = random.randint(0, 2)

if person == 0 and computer == 1:  # 多条件
    print("厉害了..你赢了")
    pass
elif person == 1 and computer == 2:
    print("厉害了..你赢了")
elif person == 2 and computer == 0:
    print("厉害了..你赢了")
    pass
elif person == computer:
    print('不错 居然是平手')
    pass
else:
    print('哈哈...你输了吧')
    pass
