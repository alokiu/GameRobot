from pygame.sprite import Sprite
from pygame import image

class Block(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = image.load('gir.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
