#!/home/djr/anaconda3/bin/python
'''
目标 1窗口 2图片 3绘图 4鼠标 5按键 6事件 7精灵组
'''
import pygame
from pygame.locals import*
from sys import exit

color = (0,0,255)
#初始化窗口模块
pygame.display.init()
#修改黑框大小 RESIZABLE随意拖动修改大小
screen=pygame.display.set_mode((480,700),RESIZABLE,0)
#修改黑框标题
pygame.display.set_caption("飞机大战")
#改变背景图片加载背景图片
bg=pygame.image.load('//home/djr/dir/feijidazhan/tupian/bg.png').convert()
#背景图片大小 坐标 尺寸  向窗口绘制背景图片
screen.blit(bg,(0,0))
#画矩形 最后一个参数是宽度 0 是实心 非0空心
pygame.draw.rect(screen,color,(10,10,20,20),1)
#变鼠标图标
ms = pygame.image.load('//home/djr/dir/feijidazhan/tupian/life.png').convert_alpha()
#设置鼠标隐藏
pygame.mouse.set_visible(False)

while True:
    #画背景 绘画顺序
    screen.blit(bg,(0,0))
    r = screen.get_rect()
    #画矩形
    pygame.draw.rect(screen,color,(r.centerx- 100,r.centery - 100,200,200),1)
    #获得鼠标位置
    x,y = pygame.mouse.get_pos()
    #绘制鼠标图标
    screen.blit(ms,(x,y))
    #print(pygame.mouse.get_pressed()) 打印鼠标触发
    #获得所有事件
    for event  in pygame.event.get():
        print(event)
        if event.type == QUIT:
            exit()
         #判断是否鼠标按下事件   
        if event.type == MOUSEBUTTONDOWN:
            (x1,y1)=event.pos
            draw_rect=pygame.Rect(r.centerx- 100,r.centery- 100,200,200)
            #检测鼠标是否点击矩形区域
            if draw_rect.collidepoint(x1,y1):
                if color==(0,0,255):
                    color=(255,0,0)
                else:
                    color = (0,0,255)
    #更新界面
    pygame.display.update()
