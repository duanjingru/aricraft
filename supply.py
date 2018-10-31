'''
供给品
'''
import pygame
import bullet
from random import randint
from pygame.locals import*
class Bomb_supply(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,width,height):
        self.image=pygame.image.load('tupian/bomb_supply.png').convert_alpha()
        self.bombimage = pygame.image.load('tupian/bomb.png').convert_alpha()
        self.soundget=pygame.mixer.Sound('sound/get_bomb.wav')
        self.sounduse=pygame.mixer.Sound('sound/use_bomb.wav')
        self.active=False
        self.speed=3
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.x=randint(0,width-self.rect.width)
        self.rect.y=randint(- 5*height,0)
        self.width=width
        self.height=height
        self.num =0
    def move(self):
        if not self.active:
            return
        self.rect.y += self.speed
        if self.rect.y > self.height:
            self.reset()

    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
            
    def draw_bomb(self,surface):
        if self.num == 1:
            surface.blit(self.bombimage,(320,650))
        elif self.num == 2:
            surface.blit(self.bombimage,(360,650))
            surface.blit(self.bombimage,(320,650))
        elif self.num ==3:
            surface.blit(self.bombimage,(400,650))
            surface.blit(self.bombimage,(360,650))
            surface.blit(self.bombimage,(320,650))

    def reset(self):
        self.rect.x = randint(0,self.width-self.rect.width)
        self.rect.y = randint(- 5*self.height,0)
        self.active = False

    def collide(self,mplane):    
        if pygame.sprite.collide_mask(self,mplane):
            if self.num < 3:
                self.num += 1
                self.soundget.play()
                self.soundget.set_volume(0.9)
                self.active = False
                self.reset()
            if self.num==3:
                self.active=True

    def use(self,enmgroup):
        if self.num > 0:
            self.num -= 1
            for enm in enmgroup:
                if enm.rect.y > 0:
                    enm.active = False

class Bullet_supply(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,width,height):
        self.image=pygame.image.load('tupian/bullet_supply.png').convert_alpha()
        self.soundget=pygame.mixer.Sound('sound/get_bullet.wav')
        self.active=False
        self.speed=3
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.x=randint(0,width-self.rect.width)
        self.rect.y=randint(- 10*height,- 5*height)
        self.width=width
        self.height=height
        self.num =0
        
    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)

    def move(self):
        if not self.active:
            return
        self.rect.y += self.speed
        if self.rect.y > self.height:
            self.reset()
    def draw_bullet(self,surface):
        if self.num == 1:
            surface.blit(self.image,(400,100))

    def reset(self):
        self.rect.x = randint(0,self.width-self.rect.width)
        self.rect.y = randint(- 10*self.height,- 5*self.height)
        self.active = False
    def collide(self,mplane):
        if pygame.sprite.collide_mask(self,mplane):
            if self.num < 1:
                self.num += 1
                self.soundget.play()
                self.soundget.set_volume(0.9)
                self.active = False
                self.reset()
            if self.num == 1:
                self.active = True
    def use(self,bullet2_list):
        if self.num>0:
            self.num -= 1






        


