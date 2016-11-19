from pygame.sprite import Sprite, collide_rect
from pygame import Surface

jumpPower = 10
gravity = 0.4

class Hero(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((20,20))
        self.image.fill((150,0,0))
        self.xSpeed = 1
        self.ySpeed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
    def update(self, up, platforms):
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
    def collide(self, xSpeed, ySpeed, platdorms):
        for object in platdorms:
            if collide_rect(self, object):
                if xSpeed > 0:
                    self.rect.right = object.rect.left
                if xSpeed < 0:
                    self.rect.left = object.rect.right
                if ySpeed > 0:
                    self.rect.bottom  = object.rect.top
                    self.onGround = True
                    self.ySpeed = 0
                if ySpeed < 0:
                    self.rect.top = object.rect.bottom
                    self.ySpeed = 0


