import pygame
import random


from study08_案例planeGame.ch02_面向对象.enemyBullet import EnemyBullet


# 创建敌机类

class EnemyPlane(object):

    def __init__(self, screen):
        # 飞机默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.imageName = '../feiji/enemy0.png'
        self.image = pygame.image.load(self.imageName)

        self.bulletList = []

        # 默认设置一个方向，左右来走
        self.direction = 'right'
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        '''
        因为要发子弹
        则 完善子弹的展示逻辑
        '''
        needDelItemList = []  # 删除的子弹列表
        for item in self.bulletList:
            if item.judge():  # 为 true 时，越界，加入到删除列表中
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
        pass



    def sheBullet(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num = random.randint(1, 50)
        if num == 3:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)
        pass

    def move(self):
        '''
        敌机移动，随机进行
        :return:
        '''
        if self.direction == 'right':
            self.x += 1
            pass
        elif self.direction == 'left':
            self.x -= 1
            pass

        if self.x > 350 - 20:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        pass

    pass
