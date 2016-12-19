from pygame.sprite import Sprite, collide_rect
from pygame import Surface

jumpPower = 10
gravity = 0.4

class Hero(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((20,20))
        self.image.fill((150,0,0))
        self.__xSpeed = 2
        self.__ySpeed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__onGround = False
        self.__live = True
        self.__points = 0
        self.__up = False

    @property
    def xSpeed(self):
        return self.__xSpeed

    @xSpeed.setter
    def xSpeed(self, new_mass):
        if (isinstance(new_mass, float)):
            self.__xSpeed = new_mass
        elif (isinstance(new_mass, int)):
            self.__xSpeed = new_mass

    @property
    def ySpeed(self):
        return self.__ySpeed

    @ySpeed.setter
    def ySpeed(self, new_mass):
        if (isinstance(new_mass, float)):
            self.__ySpeed = new_mass
        elif (isinstance(new_mass, int)):
            self.__ySpeed = new_mass

    @property
    def onGround(self):
        return self.__onGround

    @onGround.setter
    def onGround(self, new_mass):
        if (isinstance(new_mass, bool)):
            self.__onGround = new_mass

    @property
    def live(self):
        return self.__live

    @live.setter
    def live(self, new_mass):
        if (isinstance(new_mass, bool)):
            self.__live = new_mass

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_mass):
        if (isinstance(new_mass, bool)):
            self.__points = new_mass

    @property
    def up(self):
        return self.__up

    @up.setter
    def up(self, new_mass):
        if (isinstance(new_mass, bool)):
            self.__up = new_mass

    def update(self, platforms, group):
        if self.__up:
            if self.onGround:
                self.__ySpeed -= jumpPower
        if not self.onGround:
            self.__ySpeed += gravity
        self.__onGround = False
        self.rect.x += self.__xSpeed
        self.collide(self.__xSpeed, 0, platforms)
        self.rect.y += self.__ySpeed
        self.collide(0, self.__ySpeed, platforms)
        self.killCollision(group)
        self.__points += self.__xSpeed * 0.05
    def collide(self, xSpeed, ySpeed, platdorms):
        for object in platdorms:
            if collide_rect(self, object):
                if ySpeed > 0:
                    self.rect.bottom  = object.rect.top
                    self.__onGround = True
                    self.__ySpeed = 0
    def killCollision(self,group):
        for object in group:
                if self.rect.bottom == object.rect.top:
                    self.__live = False
                    self.__xSpeed = 2
                    self.__ySpeed = 0
                    self.rect.x = 55
                    self.rect.y = 55
                    self.__onGround = False
                    self.__points = 0
                    self.__up = False





