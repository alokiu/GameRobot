import pygame,sys

pygame.font.init()

class Help():
    @staticmethod
    def helpToGame(screen, window):
        done = True
        font_help = pygame.font.SysFont('Calibre', 80, True, True)
        while done:
            screen.blit(pygame.image.load('image\menu2.jpg'), (0, 0))
            for e in pygame.event.get():
                if e.type  == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        done = False
            screen.blit(font_help.render(u'HELP ', 1, (250,0,0)), (290, 85))
            screen.blit(font_help.render(u'SPACE - jump ', 1, (0,250,0)), (80, 195))
            screen.blit(font_help.render(u'P - pause ', 1, (0,250,0)), (80, 295))
            screen.blit(font_help.render(u'Esc - access the menu ', 1, (0,250,0)), (80, 395))

            window.blit(screen, (0, 0))
            pygame.display.flip()