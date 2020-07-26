import pygame
from pygame.locals import *


def key_control(heroPlane):
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.type == K_LEFT:
                print('left')
                heroPlane.move_left()  # 调用函数实现左移动
                pass
            elif event.type == K_d or event.type == K_RIGHT:
                print('right')
                heroPlane.move_right()  # 调用函数实现右移动
                pass
            elif event.key == K_SPACE:
                print('按下了空格键 space 发射子弹')
                heroPlane.she_bullet()
        pass
    pass
