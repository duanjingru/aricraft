'''
敌机类
'''
import pygame
from random import randint
class Enemy(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tupian/enemy1.png').convert_alpha()
        self.destroy_list=[
                pygame.image.load('tupian/enemy1_down1.png').convert_alpha(),
                pygame.image.load('tupian/enemy1_down2.png').convert_alpha(),
                pygame.image.load('tupian/enemy1_down3.png').convert_alpha(),
                pygame.image.load('tupian/enemy1_down4.png').convert_alpha()]
        self.destroy_index=0                    
        self.sound = pygame.mixer.Sound('sound/enemy1_down.wav')
        self.rect=self.image.get_rect()
        self.rect.x=randint(0,width - self.rect.width)
        self.rect.y=randint(- 5 *height,0)
        self.active=True
        self.speed=2
        self.width = width
        self.height = height
        self.mask=pygame.mask.from_surface(self.image)
        self.flag=1
        self.score = 0
    def move(self):
        self.rect.y +=self.speed
        if self.rect.y > self.height:
            self.reset()
    def draw_active(self,surface):
        surface.blit(self.image,self.rect)

    def draw_destroy(self,surface):
        if self.destroy_index<24:
            surface.blit(self.destroy_list[self.destroy_index//6],self.rect)
            self.destroy_index+=1
        else:
            self.reset()
            self.score = 10
            

    def draw(self,surface):
        if self.active:
            self.draw_active(surface)
        else:
            self.sound.play()
            self.sound.set_volume(0.9)
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index = 0
        self.rect.x = randint(0,self.width - self.rect.width)
        self.rect.y = randint(- 5*self.height,0)
        self.active = True
        self.score =0
        self.flag = 1
        self.sound = pygame.mixer.Sound('sound/enemy1_down.wav')
class Enemy2(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('tupian/enemy2.png').convert_alpha()
        self.image2 = pygame.image.load('tupian/enemy2_hit.png').convert_alpha()
        self.destroy_list=[
                pygame.image.load('tupian/enemy2_down1.png').convert_alpha(),
                pygame.image.load('tupian/enemy2_down2.png').convert_alpha(),
                pygame.image.load('tupian/enemy2_down3.png').convert_alpha(),
                pygame.image.load('tupian/enemy2_down4.png').convert_alpha(),
                ]
        self.destroy_index = 0
        self.sound = pygame.mixer.Sound('sound/enemy2_down.wav')
        self.rect = self.image1.get_rect()
        self.rect.x = randint(0,width - self.rect.width)
        self.rect.y = randint(- 10 *height,- 5*height)
        self.active = True
        self.speed = 2
        self.width = width
        self.height = height
        self.mask = pygame.mask.from_surface(self.image1)
        self.flag = 2
        self.score = 0
        self.life = 5
    def move(self):
        self.rect.y += self.speed
        if self.rect.y > self.height:
            self.reset()
    def draw_active(self,surface):
        if self.life<6:
            if self.life == 5:
                surface.blit(self.image1,self.rect)
            elif 0<self.life<5:
                surface.blit(self.image2,self.rect)
    
    def draw_destroy(self,surface):
        if self.destroy_index<24:
            surface.blit(self.destroy_list[self.destroy_index//6],self.rect)
            self.destroy_index+=1
        else:
            self.reset()
            self.score = 100

    def draw(self,surface):
        if self.active:
                self.draw_active(surface)
        else:
            self.sound.play()
            self.sound.set_volume(0.9)
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index = 0
        self.rect.x = randint(0,self.width - self.rect.width)
        self.rect.y = randint(- 10*self.height,- 5*self.height)
        self.active = True
        self.flag = 2
        self.score =0
        self.life = 5    
        self.sound = pygame.mixer.Sound('sound/enemy2_down.wav')
class Enemy3(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image3 = pygame.image.load('tupian/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('tupian/enemy3_n2.png').convert_alpha()
        self.image1 = pygame.image.load('tupian/enemy3_hit.png').convert_alpha()
        self.destroy_list=[
                pygame.image.load('tupian/enemy3_down1.png').convert_alpha(),
                pygame.image.load('tupian/enemy3_down2.png').convert_alpha(),
                pygame.image.load('tupian/enemy3_down3.png').convert_alpha(),
                pygame.image.load('tupian/enemy3_down4.png').convert_alpha(),
                pygame.image.load('tupian/enemy3_down5.png').convert_alpha(),
                pygame.image.load('tupian/enemy3_down6.png').convert_alpha(),
                ]
        self.destroy_index = 0
        self.sound = pygame.mixer.Sound('sound/enemy3_down.wav')
        self.soundfly = pygame.mixer.Sound('sound/enemy3_flying.wav')
        self.rect = self.image1.get_rect()
        self.rect.x = randint(0,width - self.rect.width)
        self.rect.y = randint(- 20 *height,- 15*height)
        self.active = True
        self.speed = 1
        self.width = width
        self.height = height
        self.mask = pygame.mask.from_surface(self.image1)
        self.flag = 3
        self.score = 0
        self.life = 15

    def move(self):
        self.rect.y += self.speed
        if self.rect.y >0:
            self.soundfly.play()
            self.soundfly.set_volume(0.8)
        if self.rect.y > self.height:
            self.reset()
            self.soundfly.stop()
    def draw_active(self,surface):
        if self.life<16:
            if 10<self.life<=15:
                surface.blit(self.image1,self.rect)
                pygame.draw.rect(surface,(255,0,0),(self.rect.x,self.rect.y- 20,150,5),0)
                pygame.draw.rect(surface,(0,0,255),(self.rect.x,self.rect.y- 20,150,5),1)

            elif 5<self.life<=10:
                surface.blit(self.image2,self.rect)
                pygame.draw.rect(surface,(0,0,255),(self.rect.x,self.rect.y- 20,150,5),1)
                pygame.draw.rect(surface,(255,0,0),(self.rect.x,self.rect.y- 20,100,5),0)
            elif 0<self.life<=5:
                surface.blit(self.image3,self.rect)
                pygame.draw.rect(surface,(0,0,255),(self.rect.x,self.rect.y- 20,150,5),1)
                pygame.draw.rect(surface,(255,0,0),(self.rect.x,self.rect.y- 20,50,5),0)
    def draw_destroy(self,surface):
        if self.destroy_index<36:
            surface.blit(self.destroy_list[self.destroy_index//6],self.rect)
            self.destroy_index+=1
        else:
            self.reset()
            self.soundfly.stop()
            self.score = 300

    def draw(self,surface):
        if self.active:
                self.draw_active(surface)
        else:
            self.sound.play()
            self.sound.set_volume(0.9)
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index = 0
        self.rect.x = randint(0,self.width - self.rect.width)
        self.rect.y = randint(- 20*self.height,- 15*self.height)
        self.active = True
        self.score =0
        self.flag = 3
        self.life = 15
        self.sound = pygame.mixer.Sound('sound/enemy3_down.wav')




    



