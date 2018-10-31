#!/home/djr/anaconda3/bin/python
'''
目标 1窗口 2图片 3绘图 4鼠标 5按键 6事件 7精灵组
'''
import pygame
from pygame.locals import*
from sys import exit
from random import randint
#初始化窗口模块
pygame.init()
#音乐模块的初始化
pygame.mixer.init()
#构造函数接受一个新的事件类型
ADD2EVENT=pygame.event.Event(26,s=(randint(- 1,1),randint(- 1, 1)))
#创建一个新的事件 比USEREVENT大
ADDEVENT = USEREVENT + 1
#创建一个1秒计时器定时向事件队列发送事件 第二个参数为零时 停止发送事件  
pygame.time.set_timer(ADDEVENT,2*1000)
pygame.time.set_timer(ADD2EVENT.type,3*10)

#修改黑框大小 RESIZABLE随意拖动修改大小
screen=pygame.display.set_mode((480,700),RESIZABLE,0)
#修改黑框标题
pygame.display.set_caption("飞机大战")
#改变背景图片加载背景图片
bg=pygame.image.load('//home/djr/dir/feijidazhan/tupian/bg.png').convert()
#设置鼠标隐藏
pygame.mouse.set_visible(False)
x,y =300,300
l=[
pygame.image.load('//home/djr/dir/feijidazhan/tupian/me_destroy_1.png').convert_alpha(),
pygame.image.load('//home/djr/dir/feijidazhan/tupian/me_destroy_2.png').convert_alpha(),
pygame.image.load('//home/djr/dir/feijidazhan/tupian/me_destroy_3.png').convert_alpha(),
pygame.image.load('//home/djr/dir/feijidazhan/tupian/me_destroy_4.png').convert_alpha()]
index = 0

rnum = lambda x : randint(1,x)
#生成clock对象 ，用于控制时间 控制帧率 生成clock对象 调用tick 方法
clock = pygame.time.Clock()
'''
生成移动的小球
准备列表保存这些小球
一个小球c={x,y,r,vx,vy}  x,y圆心 vx,vy 速度 半径 r'''
circlelist=[]
#创建一个圆的类
class circle:
    def __init__(self):
        self.x=randint(- 480,480)
        self.y=randint(- 700,700)
        self.vx=randint(- 2, 2)
        self.vy=randint(- 2, 2)
        self.r=randint(1,8)
        self.color=(rnum(255),rnum(255),rnum(255))
        self.shixin = randint(0,1)
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,self.shixin)


#加载字库

f = pygame.font.Font('//home/djr/dir/feijidazhan/font/CHILLER.TTF',32)
text = 'I love you'
#第一个参数文本 第二个 第三个颜色 第四个背景颜色,第五个位置
bg.blit(f.render(text,True,(255,0,0)),(100,100))


#加载音乐
sound = pygame.mixer.Sound('//home/djr/dir/feijidazhan/sound/bullet.wav')
sound.set_volume(0.7)
pygame.mixer.music.load('//home/djr/dir/feijidazhan/sound/game_music.ogg')
sound.set_volume(0.5)
pygame.mixer.music.play()
while True:
    screen.blit(bg,(0,0))
    #画矩形 screen :在屏幕上画  0,0,255: 颜色  x,y,坐标  40,40大小 0填充
    pygame.draw.rect(screen,(0,0,255),(x,y,40,40),1)
    keys = pygame.key.get_pressed()
    if keys[K_w] == 1:
        y-=3
        #按键播放音效
        sound.play()
    if keys[K_s] == 1:
        y+=3
        #暂停背景音乐 按键
        pygame.mixer.music.unpause()
    if keys[K_a] == 1:
        x-=3
        #按键开始背景音乐
        pygame.mixer.music.pause()
    if keys[K_d] == 1:
        x+=3
    
        
    #画图 使图片依次出现
    if index<4:
        bg.blit(l[index],(30,30))
        index += 1

    #获得所有事件   
    for event  in pygame.event.get():
        print(event)
        if event.type == QUIT:
            exit()
        elif event.type == ADDEVENT:
            #pygame.draw.circle(bg,(123,123,123),(randint(0,480),randint(0,700)),5)
            print('event1')
        elif event.type == ADD2EVENT.type:
            c=circle()
            circlelist.append(c)
    rect = pygame.rect.Rect(x,y,40,40)
	#画小球
    for cir in circlelist:#改变位置
        if rect.collidepoint(cir.x,cir.y):
            circlelist.remove(cir)
        else:
            cir.move()
            cir.draw(screen)
	

        
    #更新界面
    pygame.display.update()
    #pygame.time.delay(1000)延时
    #延时 控制帧率 生成clock对象 调用tick方法
    clock.tick(1000)
