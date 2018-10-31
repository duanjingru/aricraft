'''
飞机大战

'''
import re
import pygame
import myplane
import enemy 
import supply
import bullet
from sys import exit
from pygame.locals import*
from time import ctime
#初始化pygame
pygame.init()

#绘制屏幕 背景 
screen = pygame.display.set_mode((480,700),RESIZABLE,0)
bg1 = pygame.image.load('tupian/bg.png').convert()
#bg2 = pygame.image.load('tupian/bg.png').convert()
#bg3 = pygame.image.load('tupian/bg.png').convert()

#修改黑框标题
pygame.display.set_caption('飞机大战')
#绘制开始暂停键
resume_nor = pygame.image.load('tupian/resume_nor.png').convert_alpha()

pause_nor = pygame.image.load('tupian/pause_nor.png').convert_alpha()


resume_pressed = pygame.image.load('tupian/resume_pressed.png').convert_alpha()

pause_pressed = pygame.image.load('tupian/pause_pressed.png').convert_alpha()
#结束游戏背景图
again = pygame.image.load('tupian/again.png').convert_alpha()
again_rect = again.get_rect()
again_rect.x,again_rect.y = (90,330)
gameover = pygame.image.load('tupian/gameover.png').convert_alpha()
gameover_rect = gameover.get_rect()
gameover_rect.x,gameover_rect.y = (90,390)
#字体加载
font = pygame.font.Font('font/font.ttf',32)
font2 = pygame.font.Font('font/CHILLER.TTF',72)
font3 = pygame.font.Font('font/simhei.ttf',24)
scoreover =0
i = 30
#加载资源
def main():
    x1,y1 = 0,0
    #背景音乐
    pygame.mixer.music.load('sound/game_music.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #循环的帧
    clock = pygame.time.Clock()
    mplane = myplane.Myplane(480,700)
    #四个子弹
    bullet_list=[bullet.Bullet(mplane.rect) for x in range(4)]
    bullet_index=0
    delay=0
    bullet2_list = [bullet.Bullet2(mplane.rect) for x in range(4)]
    bullet2_index=0
    bullet2_num=4
    num = 0
    delayy = 0
    bullet3_list = [bullet.Bullet3(mplane.rect) for x in range(4)]
    bullet3_index=0
    delay1 = 0
    B=[]
    A=[]
    C=[]
    #敌机生成精灵组
    enemys_group=pygame.sprite.Group([enemy.Enemy(480,700) for x in range(10)],
            [enemy.Enemy2(480,700) for x in range(5)],
            [enemy.Enemy3(480,700) for x in range(4)])    
    #供给品生成   
    bomb = supply.Bomb_supply(480,700)
    BOMBSUPPLYEVENT = USEREVENT+1
    pygame.time.set_timer(BOMBSUPPLYEVENT,35*1000)
    bullet2 = supply.Bullet_supply(480,700)
    BULLETSUPPYEVENT = USEREVENT +2
    pygame.time.set_timer(BULLETSUPPYEVENT,60*1000)
    score = 0
    #背景轮播
    bg1 = pygame.image.load('tupian/bg.png').convert()
    bg2 = pygame.image.load('tupian/bg.png').convert()
    bg3 = pygame.image.load('tupian/bg.png').convert()
    bg = [bg1,bg2,bg3]
    while True:
        y1 += 1
        if y1>700:
            bg = bg[1:]+bg[:1]
            bg1,bg2,bg3 = bg
            y1 = 0
        screen.blit(bg1,(x1,y1))
        screen.blit(bg2,(x1,y1- 700))
        screen.blit(bg3,(x1,y1- 1400))
        
        screen.blit(pause_nor,(400,20))

        mplane.draw_life(screen)
        for event in pygame.event.get():
            #退出
            if event.type == QUIT:
                exit()
            elif event.type == BOMBSUPPLYEVENT:
                bomb.active=True
            elif event.type ==  KEYDOWN:
                if event.key == K_SPACE:
                    bomb.use(enemys_group)
                    bomb.sounduse.play()
                    bomb.sounduse.set_volume(0.9)
            
            elif event.type == BULLETSUPPYEVENT:
                bullet2.active = True
        #开始暂停
        x = True
        keys = pygame.key.get_pressed()
        if keys[K_b]:
            screen.blit(bg1,(0,0))
            screen.blit(font2.render("score:"+str(score),True,(255,0,0)),(100,200))
            screen.blit(font3.render("W: 向上移动    S:向下移动",True,(0,0,0)),(30,500))
            screen.blit(font3.render("A: 向左移动    D:向右移动",True,(0,0,0)),(30,600))
            screen.blit(font3.render("B: 暂停        M:开始",True,(0,0,0)),(30,100))

            screen.blit(font3.render("空格： 使用炸弹",True,(0,0,0)),(30,400))
            screen.blit(resume_nor,(400,20))
            screen.blit(resume_pressed,(200,300))
            pygame.mixer.music.stop()
            while x:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type ==  KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[K_m]:
                            screen.blit(pause_nor,(400,20))
                            screen.blit(pause_pressed,(200,300))
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(0.2)
                            x = False
                pygame.display.flip()

                    
        #飞机
        mplane.move()
        mplane.collide(enemys_group)
        mplane.draw(screen)
        #子弹


        if bullet2.num== 0:
            if  not delay % 12:
                bullet_list[bullet_index% 4].reset(mplane.rect)
                bullet_index +=1

            for b in bullet_list:
                b.move()
                b.collide(enemys_group)
                b.draw(screen)
                B.append(b)
            delay+=1
        
        
        
        else:
            if not delayy % 12:
                bullet2_list[bullet2_index% 4].reset(mplane.rect)
                bullet2_index +=1
                num += bullet2_num
            for l in bullet2_list:
                l.move()
                l.collide(enemys_group)
                l.draw(screen)
                A.append(l)
            delayy+=1
            
            
            if not delay1 % 12:
                bullet3_list[bullet3_index% 4].reset(mplane.rect)
                bullet3_index +=1
            for p in bullet3_list:
                p.move()
                p.collide(enemys_group)
                p.draw(screen)
                C.append(p)
            delay1+=1
            if num>=399:
                bullet2.use(bullet2_list)
                for x in A:
                    x.reset(mplane.rect)
                    x.active = False
                A=[]
                bullet2_index = 0
                bullet2.use(bullet3_list)
                for x in C:
                    x.reset(mplane.rect)
                    x.active = False
                C=[]
                for x in B:
                    x.reset(mplane.rect)
                    x.active = False
                B=[]
                bullet3_index =0
                bullet_index = 0
                num = 0
        #敌机
        for e in enemys_group:
            e.move()
            e.draw(screen)
            if e.score != 0:
                score += e.score
                e.score = 0
        global scoreover
        scoreover= score
        #供给物
        bomb.move()
        bomb.collide(mplane) 
        bomb.draw_bomb(screen)
        bomb.draw(screen)
        #双发子弹
        bullet2.move()
        bullet2.collide(mplane)
        bullet2.draw_bullet(screen)
        bullet2.draw(screen)


        
        #打印分数        
        screen.blit(font.render("score:"+str(score),True,(0,0,0)),(20,5))
        if mplane.life_num == 0:
            f=open('score.txt','a')
            f.write('\t分数为:'+str(scoreover)+'\t时间为：'+ctime()+'\n')
            f.close()
            break
        pygame.display.flip()
        if scoreover<=3000:
            i = 60
            clock.tick(i)
        if 3000<scoreover<5000:
            i = 90
            clock.tick(i)
        if 5000<=scoreover<=10000:
            i = 120
            clock.tick(i)
        if 10000<scoreover:
            if i<1000:
                i+=1
                clock.tick(i)

            
            





def game():
    while True:
        main()
        pygame.mixer.music.stop()
        #退出游戏
        screen.blit(bg1,(0,0))
        screen.blit(again,again_rect)
        screen.blit(gameover,gameover_rect)
        screen.blit(font2.render("score:"+str(scoreover),True,(0,0,0)),(90,200))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            if pygame.mouse.get_pressed()[0]:
                mx,my = pygame.mouse.get_pos()
                if again_rect.collidepoint(mx,my):
                    break
                if gameover_rect.collidepoint(mx,my):
                    pygame.quit()
                    exit()
game()


#初始化
#游戏循环
#退出游戏
