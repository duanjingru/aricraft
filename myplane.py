'''
飞机类
'''
import pygame
from pygame.locals import*


#继承精灵组类
class Myplane(pygame.sprite.Sprite):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        #飞机动态图片
        self.image1 = pygame.image.load('tupian/me1.png').convert_alpha()
        self.image2 = pygame.image.load('tupian/me2.png').convert_alpha()
        #飞机销毁图片
        self.destroy_images=[
                pygame.image.load('tupian/me_destroy_1.png').convert_alpha(),
                pygame.image.load('tupian/me_destroy_2.png').convert_alpha(),
                pygame.image.load('tupian/me_destroy_3.png').convert_alpha(),
                pygame.image.load('tupian/me_destroy_4.png').convert_alpha()]
        self.lifeimage = pygame.image.load('tupian/life.png').convert_alpha()
        #飞机音效
        self.sound = pygame.mixer.Sound('sound/me_down.wav')
        #飞机位置
        self.rect = self.image1.get_rect()
        self.rect.x = (self.width-self.rect.width)/2
        self.rect.y = self.height- 180
        #飞机速度
        self.speed = 10
        #状态默认活跃
        self.active = True
        #生命值
        self.life_num = 3
        #飞机动态转换标记
        self.switch = 0
        self.destroy_index = 0
        self.mask = pygame.mask.from_surface(self.image1)

    def move(self):
        #获取按键 移动
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            if self.rect.y > 0:
                self.rect.y = self.rect.y - self.speed
        if keys[K_s]:
            if self.rect.y < (self.height- 180):
                self.rect.y = self.rect.y + self.speed
        if keys[K_a]:
            if self.rect.x > 0:
                self.rect.x = self.rect.x - self.speed
        if keys[K_d]:
            if self.rect.x < (self.width - self.rect.width):
                self.rect.x = self.rect.x + self.speed

    def draw(self,surface):
        if self.active:
            self.draw_active(surface)
        else:
            self.sound.play()
            self.sound.set_volume(0.9)
            self.draw_destroy(surface)
    #飞机正常的图
    def draw_active(self,surface):
        if self.switch% 2 == 0:
            surface.blit(self.image1,self.rect)
        else:
            surface.blit(self.image2,self.rect)
        #转换switch的值 实现图片转换 2秒切一次
        self.switch +=1 #0 1 2 3 4 5 6 7 余数为零时切图 
    #飞机生命值
    def draw_life(self,surface):
        if self.life_num == 3:
            surface.blit(self.lifeimage,(10,650))
            surface.blit(self.lifeimage,(50,650))
            surface.blit(self.lifeimage,(90,650))
        elif self.life_num == 2:
            surface.blit(self.lifeimage,(10,650))
            surface.blit(self.lifeimage,(50,650))
        elif self.life_num == 1:
            surface.blit(self.lifeimage,(10,650))


    #飞机销毁的图
    def draw_destroy(self,surface):
        if self.destroy_index<200:
            surface.blit(self.destroy_images[self.destroy_index//50],self.rect)
            self.destroy_index+=1
        elif self.life_num>0:
            self.life_num-=1
            self.reset()
    #复位函数 即重置函数
    def reset(self):
        self.rect.x = (self.width - self.rect.width)/2
        self.rect.y = self.height- 180
        self.active = True
        self.switch = 0
        self.destroy_index = 0
    #碰撞检测
    def collide(self,emgroups):
        emlist = pygame.sprite.spritecollide(self,emgroups,False,pygame.sprite.collide_mask)
        if emlist != []:
            self.active = False
        for em in emlist:
            em.active = False
    
        





