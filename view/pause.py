import pygame, sys

pygame.font.init()

class Pause:
    @staticmethod
    def pauseOfGame(screen, window):
        pygame.mouse.set_visible(True)
        done = True
        font_pause = pygame.font.SysFont('Calibre',80,True,True)
        while done:
            screen.blit(pygame.image.load('image\menu2.jpg'),(0,0))
            for e in pygame.event.get():
                if e.type  == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_p:
                        done = False
            screen.blit(font_pause.render(u'PAUSE ',1,(250,0,0)),(290,85))
            screen.blit(font_pause.render(u'P - Back to the game ', 1, (0,250,0)), (70, 195))
            screen.blit(font_pause.render(u'Esc - Exit the game ', 1, (0,250,0)), (85, 295))

            window.blit(screen, (0, 0))
            pygame.display.flip()