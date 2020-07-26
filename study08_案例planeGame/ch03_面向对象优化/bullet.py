import pygame

class CommonBullet(object):
    '''
    公共的子弹类
    '''
    def  __init__(self,x,y,screen,bulletType):
        self.type=bulletType
        self.screen=screen
        if self.type=='hero':
            self.x=x+13
            self.y=y-20
            self.imagePath='../feiji/bullet.png'
        elif self.type == 'enemy':
            self.x = x
            self.y =y+10
            self.imagePath = '../feiji/bullet1.png'
            pass
        self.image=pygame.image.load(self.imagePath)
        pass
    def move(self):
        '''
        子弹的移动
        :return:
        '''
        if self.type=='hero':
            self.y-=2
        elif self.type=='enemy':
            self.y+=2
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y>500 or self.y<0:
            return True
        else:
            return False
        pass
    pass