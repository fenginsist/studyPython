import pygame
from pygame.locals import *  # *号 就是 要导入 pygame.locals 中的所有


def key_control(planeObj):
    '''
    定义普通的函数 用来实现键盘的检测
    :param HeroObj:
    :return:
    '''
    # 获取键盘事件
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                planeObj.moveLeft()
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                planeObj.moveRight()
                pass
            elif event.key == K_SPACE:
                print('按下了空格键 K_SPACE 发射了子弹')
                planeObj.sheBullet()
                pass
            pass
        pass
    pass
