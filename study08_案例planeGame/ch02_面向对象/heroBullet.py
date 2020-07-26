import pygame
'''
2. 创建子弹类
'''


class Bullet(object):

    def __init__(self, x, y, screen):
        '''

        :param x:
        :param y:
        :param screen: 窗口对象
        '''
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('../feiji/bullet.png')
        pass

    def display(self):
        # 这里的位置 也就是 飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y -= 2
        pass

    def judge(self):
        '''
        判断 子弹是否越界
        子弹上移，逐渐上升，Y 值 减小，小于 0 时，就是越界，然后删除掉
        :return:
        '''
        if self.y < 0:  # 越界
            return True
        else:
            return False  # 不越界
        pass

    pass
