import pygame

from study08_案例planeGame.ch02_面向对象.heroBullet import Bullet

'''
1、实现飞机的显示 并且可以控制飞机的移动【面向对象】
'''


class hero_plane(object):

    def __init__(self, screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        '''
        飞机的默认位置，坐标轴：左上角 为（0， 0）, 左右为 x 轴，上下为 y 轴
        右 下 皆为正，没有负数
        '''
        self.x = 150
        self.y = 450
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.imagesName = '../feiji/hero.png'
        self.image = pygame.image.load(self.imagesName)

        # 用来存放子弹的列表
        self.bulletList = []
        pass

    def moveLeft(self):
        '''
        左移动
        :return:
        '''
        if self.x > 0:
            self.x -= 10
        pass

    def moveRight(self):
        '''
        右移动
        :return:
        '''
        if self.x < 350 - 40:
            self.x += 10
        pass

    # 注意一下 重点 下面有更改
    def display(self):
        '''
        在主窗口中显示飞机
        :return:
        '''
        #
        self.screen.blit(self.image, (self.x, self.y))

        '''
        因为要发子弹
        则 完善子弹的展示逻辑
        '''
        needDelItemList = []  # 删除的子弹列表
        for item in self.bulletList:
            if item.judge(): # 为 true 时，越界，加入到删除列表中
                needDelItemList.append(item)
                pass
            pass

        # 重新遍历一下， 在 子弹列表中 进行删除
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass

        # 显示子弹
        for bullet in self.bulletList:
            # 显示子弹的位置
            bullet.display()
            # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
            bullet.move()
        pass

    # 发射子弹
    def sheBullet(self):
        # 创建一个新的子弹对象
        newBullet = Bullet(self.x+12, self.y, self.screen)
        # 将子弹 加入 子弹列表中
        self.bulletList.append(newBullet)
        pass

    pass
