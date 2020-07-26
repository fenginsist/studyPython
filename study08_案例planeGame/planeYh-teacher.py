import  pygame #引用第三方的模块
import random #随机产生数据的对象
import time
from pygame.locals import *
'''
1: 实现飞机的显示  并且可以控制飞机的移动【面向对象】
'''
#抽象出来一个飞机的基类
class BasePlane(object):
    def __init__(self,screen,imagePath):
        '''
        初始化基类函数
        :param screen: z主窗体对象
        :param imageName:加载的图片
        '''
        self.screen=screen
        self.image=pygame.image.load(imagePath)
        self.bulletList=[] #存储所有的子弹
        pass
    def  display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
        pass
    pass

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
            self.imagePath='./feiji/bullet.png'
        elif self.type == 'enemy':
            self.x = x
            self.y =y+10
            self.imagePath = './feiji/bullet1.png'
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

class HeroPlane(BasePlane):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        super().__init__(screen,'./feiji/hero.png') #调用父类的构造方法
        # 飞机的默认位置
        self.x=150
        self.y=450
        pass
    def moveleft(self):
        '''
        左移动
        :return:
        '''
        if self.x>0:
            self.x-=10
        pass
    def moveright(self):
        '''
        右移动
        :return:
        '''
        if self.x<350-40:
            self.x+=10
        pass
   # 发射子弹
    def sheBullet(self):
        # 创建一个新的子弹对象
        newBullet=CommonBullet(self.x,self.y,self.screen,'hero')
        self.bulletList.append(newBullet)
        pass
    pass

# 创建敌机类
class EnemyPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(screen,'./feiji/enemy0.png')
        # 默认设置一个方向
        self.direction='right'
        # 飞机的默认位置
        self.x = 0
        self.y = 0
        pass

    def sheBullet(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num=random.randint(1,50)
        if num==3:
            newBullet=CommonBullet(self.x,self.y,self.screen,'enemy')
            self.bulletList.append(newBullet)
        pass
    def move(self):
        '''
        敌机移动 随机进行的
        :return:
        '''
        if self.direction=='right':
            self.x+=2
            pass
        elif self.direction=='left':
            self.x-=2
            pass
        if self.x>350-20:
            self.direction='left'
            pass
        elif self.x<0:
            self.direction='right'
        pass

    pass


def key_control(HeroObj):
    '''
    定义普通的函数  用来实现键盘的检测
    :param HeroObj: 可控制检测的对象
    :return:
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveleft() #调用函数实现左移动
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveright() #调用函数实现右移动
                pass
            elif event.key == K_SPACE:
                print('按下了空格键 space 发射子弹')
                HeroObj.sheBullet()
    pass

def main():
    #首先创建一个窗口 用来显示内容
    screen=pygame.display.set_mode((350,500),depth=32)
    # 创建一个背景图片对象
    background=pygame.image.load('./feiji/background.png')
    # 设置一个title
    pygame.display.set_caption('阶段总结-飞机小游戏')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) #循环次数  -1表示无限循环

    # 创建一个飞机对象了
    hero=HeroPlane(screen)
    # 创建一个敌人飞机的对象
    enemyplane=EnemyPlane(screen)
    # 设定要显示的内容
    while True:
        screen.blit(background,(0,0))
        # 显示玩家飞机的图片
        hero.display()
        enemyplane.display() #显示敌机
        enemyplane.move() #敌机移动
        enemyplane.sheBullet()#敌机随机发送子弹
        # 获取键盘事件
        key_control(hero)
        # 更新显示内容
        pygame.display.update()
        # time.sleep(1) #休眠一秒钟
        pygame.time.Clock().tick(15)
    pass

if __name__=='__main__':
    main()

