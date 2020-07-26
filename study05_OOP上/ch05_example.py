# 案例：决战紫禁之巅有两个人物，西门吹雪以及叶孤城

# 属性：
# name 玩家的名字
# blood 玩家血量

# 方法：
# tong() 捅对方一刀,对方掉血10滴
# kanren() 砍对方一刀，对方掉血15滴
# chiyao() 吃一颗药，补血10滴
# __str__ 打印玩家状态。

# 第一步 需要先去定义一个类【角色类】

class Role:
    def __init__(self, name, blood):
        '''
        初始化构造函数
        :param name:  角色名
        :param blood: 血量
        '''
        self.name = name
        self.blood = blood
        pass

    def __str__(self):
        return '【%s】战士 还剩下 【%s】的血量' % (self.name, self.blood)
        pass

    def tong(self, enemy):
        '''
        捅一刀
        :param enemy: 敌人
        :return: 
        '''''
        # 敌人见到10滴血
        enemy.blood -= 10
        info = '【%s】 捅了 【%s】 一刀' % (self.name, enemy.name)
        print(info)
        pass

    def kanren(self, enemy):
        '''
        砍一刀
        :param enemy: 敌人
        :return: 
        '''''
        # 敌人见到10滴血
        enemy.blood -= 15
        info = '【%s】 砍了 【%s】 一刀' % (self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        '''
        吃药补血
        :return: 
        '''''
        self.blood += 10
        info = '【%s】 吃了一个药丸，增加10滴血' % (self.name)
        print(info)
        pass

    pass


ximenchuixue = Role('西门吹雪', 100)
yiyegucheng = Role('一叶孤城', 100)

# 西门吹雪 捅 一叶孤城 一刀
# ximenchuixue.tong(yiyegucheng)
# print(ximenchuixue)  # 打印对象的状态
# print(yiyegucheng)

# print('****************************')
# 一叶孤城 砍 西门吹雪   一刀
# yiyegucheng.kanren(ximenchuixue)
# print(ximenchuixue)  # 打印对象的状态
# print(yiyegucheng)

# print('****************************')
# 一叶孤城 吃了个药丸
# yiyegucheng.chiyao()
# print(ximenchuixue)  # 打印对象的状态
# print(yiyegucheng)

while True:

    if ximenchuixue.blood <= 0 or yiyegucheng.blood <= 0:
        break
        pass
    # 西门吹雪 捅 一叶孤城 一刀
    ximenchuixue.tong(yiyegucheng)
    print(ximenchuixue)  # 打印对象的状态
    print(yiyegucheng)

    print('****************************')
    # 一叶孤城 砍 西门吹雪   一刀
    yiyegucheng.kanren(ximenchuixue)
    print(ximenchuixue)  # 打印对象的状态
    print(yiyegucheng)

    print('****************************')
    # 一叶孤城 吃了个药丸
    yiyegucheng.chiyao()
    print(ximenchuixue)  # 打印对象的状态
    print(yiyegucheng)

    pass
