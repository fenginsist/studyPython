import pygame

from study08_案例planeGame.ch02_面向对象.heroPlane import hero_plane  # 绝对路径 正确
from study08_案例planeGame.ch02_面向对象.keyControl import key_control  # 绝对路径 正确
from study08_案例planeGame.ch02_面向对象.enemyPlane import EnemyPlane  # 绝对路径 正确


'''
from .heroPlane import hero_plane
from .keyControl import key_control

ImportError: attempted relative import with no known parent package
出现这个错误的原因主要是由于使用了相对导入包的因素：
'''


def main():
    # 1. 首先创建一个窗口对象 用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 2. 创建一个背景图片对象
    background = pygame.image.load('../feiji/background.png')
    # 3. 添加 title
    pygame.display.set_caption('阶段总结-飞机游戏')

    # 5. 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('../feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)  # 循环次数， -1 表示无限循环

    # 6. 创建一个飞机对象
    hero = hero_plane(screen)

    # 9.1 创建一个敌机对象
    enemy = EnemyPlane(screen)

    # 4. 设定要显示的内容
    while True:
        # 2.1 显示背景图片
        screen.blit(background, (0, 0))

        # 6.2 显示玩家的位置
        # screen.blit(hero, (0, 0))
        hero.display()

        # 9.2 显示敌机位置
        enemy.display()
        # 9.3 敌机随机移动
        enemy.move()
        # 9.4 敌机随机发送子弹
        enemy.sheBullet()

        # 7. 键盘检测
        key_control(hero)

        # 8. 更新显示内容
        pygame.display.update()
        # time.sleep(1) # 休眠一秒钟
        pygame.time.Clock().tick(5)
        pass
    pass


if __name__ == '__main__':
    main()
    pass
