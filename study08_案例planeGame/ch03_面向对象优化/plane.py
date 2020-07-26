import pygame


# 飞机的基类
# 两个方法  1、初始化  2、display
class BasePlane(object):

    def __init__(self, screen, imagePath):
        '''
        初始化基类函数
        :param x:
        :param y:
        :param screen: 窗口对象
        :param imagePath: 飞机图片路径
        '''
        self.screen = screen
        self.image = pygame.image.load(imagePath)

        self.bulletList = []  # 存储所有的子弹
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        # 完善子弹逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass

        # 重新 遍历，bulletList删除越界的子弹
        for item in needDelItemList:
            self.bulletList.remove(item)
            pass

        # 显示子弹位置
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
            pass
        pass

    pass
