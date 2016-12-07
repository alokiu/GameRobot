import pygame, sys

class NextLevel:
    @staticmethod
    def informationAboutNextLevel(screen, window, hero):
        pygame.mouse.set_visible(True)
        done = True
        font_nextlevel = pygame.font.SysFont('Calibre', 80, True, True)
        while done:
            screen.blit(pygame.image.load('image\menu2.jpg'), (0, 0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        done = False
            screen.blit(font_nextlevel.render(u'Next level ', 1, (250, 0, 0)), (270, 85))
            screen.blit(font_nextlevel.render(u'you score: ' + str(int(hero.points)) +'point', 1, (0, 250, 0)), (70, 195))
            screen.blit(font_nextlevel.render(u'Enter - Back to the game ', 1, (0, 250, 0)), (20, 295))

            window.blit(screen, (0, 0))
            pygame.display.flip()
