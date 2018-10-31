'''
子弹类
'''
import pygame
#单发子弹类
class Bullet(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,prect):
        self.image=pygame.image.load('tupian/bullet1.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y -= self.speed

    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
    #重置
    def reset(self,prect):
        self.rect.x = prect.centerx
        self.rect.y = prect.y
        self.active = True
    #碰撞检测
    def collide(self,enemgroup):
        if  not self.active:
            return None
        enmlist= pygame.sprite.spritecollide(self,enemgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active = False
        for enm in enmlist:
            self.sound.play()
            self.sound.set_volume(0.8)
            if enm.flag ==1:
                enm.active = False
            if enm.flag ==2:
                enm.life -= 1
                if enm.life  <= 0:
                    enm.active = False
            if enm.flag == 3:
                enm.life -=1
                if enm.life <= 0:
                    enm.active = False

class Bullet2(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,prect):
        self.image=pygame.image.load('tupian/bullet2.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx- 10
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y -= self.speed
    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
    def reset(self,prect):
        self.rect.x = prect.centerx- 10
        self.rect.y = prect.y
        self.active = True
    def collide(self,enemgroup):
        if  not self.active:
            return None
        enmlist= pygame.sprite.spritecollide(self,enemgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active = False
        for enm in enmlist:
            self.sound.play()
            self.sound.set_volume(0.8)
            if enm.flag ==1:
                enm.active = False
            if enm.flag ==2:
                enm.life -= 1
                if enm.life  <= 0:
                    enm.active = False
            if enm.flag == 3:
                enm.life -=1
                if enm.life <= 0:
                    enm.active = False
        
class Bullet3(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self,prect):
        self.image=pygame.image.load('tupian/bullet2.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx+ 10
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y -= self.speed
    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
    def reset(self,prect):
        self.rect.x = prect.centerx+ 10
        self.rect.y = prect.y
        self.active = True
    def collide(self,enemgroup):
        if  not self.active:
            return None
        enmlist= pygame.sprite.spritecollide(self,enemgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active = False
        for enm in enmlist:
            self.sound.play()
            self.sound.set_volume(0.8)
            if enm.flag ==1:
                enm.active = False
            if enm.flag ==2:
                enm.life -= 1
                if enm.life  <= 0:
                    enm.active = False
            if enm.flag == 3:
                enm.life -=1
                if enm.life <= 0:
                    enm.active = False


        
        
