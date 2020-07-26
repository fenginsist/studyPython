import pygame
import random

from study08_案例planeGame.ch03_面向对象优化.plane import BasePlane
from study08_案例planeGame.ch03_面向对象优化.bullet import CommonBullet


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, '../feiji/enemy0.png')
        # 初始化敌机位置
        self.x = 0
        self.y = 0
        # 默认设置一个方向
        self.direction = 'right'
        pass

    # 敌机移动 随机进行
    def move(self):
        '''
        敌机移动 随机进行的
        :return:
        '''
        # 移动
        if self.direction == 'right':
            self.x += 2
            pass
        elif self.direction == 'left':
            self.x -= 2
            pass

        # 设置方向
        if self.x > 350 - 20:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
        pass

    def sheBullet(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num = random.randint(1, 50)
        if num == 3:
            newBullet = CommonBullet(self.x, self.y, self.screen, 'enemy')
            self.bulletList.append(newBullet)
        pass

    pass
