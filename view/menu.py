import pygame,sys
from view.help import Help
from pygame import image

pygame.font.init()

class Menu:
    def __init__(self, punkts = [120, 140, u'Punkts', (250,250,30),(250,30,250)]):
        self.punkts = punkts
        self.image = image.load('image\menu2.jpg')
    def render(self, poverhost, font, num_punkt):
         for i in self.punkts:
             if num_punkt == i[5]:
                 poverhost.blit(font.render(i[2], 1, i[4]),(i[0], i[1]))
             else:
                 poverhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def mainMeny(self, screen, windom, hero):
        pygame.mouse.set_visible(True)
        done = True
        font_menu = pygame.font.SysFont('Tahoma',100,True,True)
        punkt = 0
        while done:
            screen.blit(self.image,(0,0))
            mouse = pygame.mouse.get_pos()
            for i in self.punkts:
                if mouse[0]>i[0] and mouse[0]<i[0]+250 and mouse[1]>i[1] and mouse[1]<i[1]+200:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type  == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt +=1
                if (e.type == pygame.MOUSEBUTTONDOWN and e.button == 1) or\
                        (e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN):
                    if punkt == 0:
                        done = False
                        hero.rect.x = 55
                    elif punkt == 1:
                        Help.helpToGame(screen, windom)
                    elif punkt == 2:
                        sys.exit()

            windom.blit(screen, (0,0))
            pygame.display.flip()
