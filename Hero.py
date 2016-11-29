from pygame.sprite import Sprite, collide_rect
from pygame import Surface

jumpPower = 10
gravity = 0.4

class Hero(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((20,20))
        self.image.fill((150,0,0))
        self.xSpeed = 2
        self.ySpeed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
    def update(self, up, space,  platforms, group):
        if up:
            if self.onGround:
                self.ySpeed -= jumpPower
        if not self.onGround:
            self.ySpeed += gravity
        self.onGround = False
        self.rect.x += self.xSpeed
        self.collide(self.xSpeed, 0, platforms)
        self.rect.y += self.ySpeed
        self.collide(0, self.ySpeed, platforms)
        self.killCollision(group)
    def collide(self, xSpeed, ySpeed, platdorms):
        for object in platdorms:
            if collide_rect(self, object):
                if ySpeed > 0:
                    self.rect.bottom  = object.rect.top
                    self.onGround = True
                    self.ySpeed = 0
    def killCollision(self,group):
        for object in group:
                if self.rect.bottom == object.rect.top:
                    print(1)





