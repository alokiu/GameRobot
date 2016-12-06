import pygame, sys

pygame.font.init()

class Pause:
    @staticmethod
    def pauseOfGame(screen, window, game, hero):
        pygame.mouse.set_visible(True)
        done = True
        font_pause = pygame.font.SysFont('Calibre',80,True,True)
        while done:
            screen.fill((100, 100, 200))
            for e in pygame.event.get():
                if e.type  == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_p:
                        done = False
            screen.blit(font_pause.render(u'PAUSE ',1,(250,0,0)),(290,85))
            screen.blit(font_pause.render(u'P - Back to the game ', 1, (250, 120, 200)), (70, 195))
            screen.blit(font_pause.render(u'Esc - Exit the game ', 1, (210, 120, 150)), (85, 295))

            window.blit(screen, (0, 0))
            pygame.display.flip()