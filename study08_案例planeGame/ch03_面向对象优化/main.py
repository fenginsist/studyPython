import pygame

from study08_案例planeGame.ch03_面向对象优化.heroPlane import HeroPlane
from study08_案例planeGame.ch03_面向对象优化.enemyPlane import EnemyPlane

from study08_案例planeGame.ch03_面向对象优化.keyControl import key_control


def Main():
    # 首先创建一个窗口 用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 创建一个背景图片对象
    background = pygame.image.load('../feiji/background.png')
    # 设置一个title
    pygame.display.set_caption('阶段总结-飞机小游戏')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('../feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # 循环次数  -1表示无限循环

    # 创建一个飞机对象了
    hero = HeroPlane(screen)
    # 创建一个敌人飞机的对象
    enemyplane = EnemyPlane(screen)
    # 设定要显示的内容
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        hero.display()

        enemyplane.display()  # 显示敌机
        enemyplane.move()  # 敌机移动
        enemyplane.sheBullet()  # 敌机随机发送子弹

        # 获取键盘事件
        key_control(hero)

        # 更新显示内容
        pygame.display.update()
        # time.sleep(1) #休眠一秒钟
        pygame.time.Clock().tick(15)
        pass
    pass


if __name__ == '__main__':
    Main()
    pass
