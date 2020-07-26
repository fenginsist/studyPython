from study08_案例planeGame.ch03_面向对象优化.plane import BasePlane
from study08_案例planeGame.ch03_面向对象优化.bullet import CommonBullet


class HeroPlane(BasePlane):

    def __init__(self, screen):
        '''
        初始化 函数
        :param screen:  主窗体
        :param imagePath:
        '''
        super().__init__(screen, '../feiji/hero.png')
        # 飞机默认位置
        self.x = 150
        self.y = 450
        pass

    def move_left(self):
        '''
        左移动
        :return:
        '''
        if self.x > 0:
            self.x -= 10
            pass
        pass

    def move_right(self):
        '''
        右移动
        :return:
        '''
        if self.x < (350 - 40):
            self.x += 10
            pass
        pass

    def she_bullet(self):
        # 创建子弹对象，并添加到 子弹列表（容器）中
        newBullet = CommonBullet(self.x, self.y, self.screen, 'hero')
        self.bulletList.append(newBullet)
        pass

    pass
