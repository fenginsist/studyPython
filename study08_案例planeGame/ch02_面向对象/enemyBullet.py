import pygame


# 敌机子弹类


class EnemyBullet(object):

    def __init__(self, x, y, sceern):

        self.x = x
        self.y = y
        self.sceern = sceern
        self.image = pygame.image.load('../feiji/bullet1.png')
        pass

    def display(self):
        '''
        显示敌机 以及 位置 子弹的信息
        :return:
        '''
        self.sceern.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y += 1
        pass

    def judge(self):
        '''
        判断 子弹是否越界
        子弹下移，逐渐下降，Y 值 增大，大于 500 时，就是越界，然后删除掉
        :return:
        '''
        if self.y > 500:
            return True  # 越界
        else:
            return False  # 没越界
        pass

    pass
