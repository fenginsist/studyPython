import pygame

from pygame.locals import *  # *号 就是 要导入 pygame.locals 中的所有


def main():
    # 1. 首先创建一个窗口对象 用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 2. 创建一个 背景图片对象
    background = pygame.image.load('./feiji/background.png')
    # 3. 添加 title
    pygame.display.set_caption('阶段总结-飞机游戏')

    # 5. 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('../feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)  # 循环次数， -1 表示无限循环

    # 6. 载入 玩家的飞机图片
    hero = pygame.image.load('./feiji/hero.png')
    # 6.1 初始化玩家的位置
    x, y = 0, 0

    # 4. 设定要显示的内容
    while True:
        # 2.1 显示背景图片
        screen.blit(background, (x, y))
        # 6.2 显示玩家图片的位置
        screen.blit(hero, (0, 0))

        # 7. 获取 键盘事件
        eventList = pygame.event.get()

        print('eventList 类型 {}'.format(type(eventList)))  # eventList 类型 <class 'list'>
        print('eventList {}'.format(eventList))  # eventList []

        # 8. 对键盘事件 进行处理
        for event in eventList:
            if event.type == QUIT: # ESC
                print('退出')
                exit()
                pass
            elif event.type == KEYDOWN:
                if event.type == K_a or event.key == K_LEFT:  # 左键
                    print('left')
                    if x > 0:
                        x -= 5
                        pass
                    pass
                elif event.type == K_d or event.key == K_RIGHT:  # 右键
                    print('right')
                    if x < 0:
                        x += 5
                        pass
                    pass
                elif event.key == K_SPACE:  # 空格键
                    print('按下了空格键 K_SPACE')
                    pass

        # 更新显示内容
        pygame.display.update()
        pygame.time.Clock().tick
        pass
    pass


if __name__ == '__main__':
    main()
    pass
